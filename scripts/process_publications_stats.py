"""
Regenerate assets/data/publications_enhanced.json.

Embeddings: sentence-transformers (local, no API key needed).
Stats:       Semantic Scholar public API (no key needed, rate-limited to 1 req/s).
AI results:  summaries and categories are defined below per-paper; extend as needed.

Usage (from repo root):
    python scripts/process_publications_stats.py
"""

import json
import re
import time
import yaml
import requests
import numpy as np
from pathlib import Path
from collections import Counter
from sklearn.decomposition import PCA
from sentence_transformers import SentenceTransformer
import umap as umap_lib

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO_ROOT        = Path(__file__).resolve().parent.parent
PUBLICATIONS_DIR = REPO_ROOT / "_publications"
STATS_CACHE      = REPO_ROOT / "_data" / "stats_cache.json"
OUTPUT_FILE      = REPO_ROOT / "assets" / "data" / "publications_enhanced.json"

S2_API_URL = "https://api.semanticscholar.org/graph/v1"

# ── Per-paper AI results (summary ≤150 chars + category) ──────────────────────
# Key = lowercase title (strip punctuation for matching).
AI_RESULTS = {
    "a hybrid generative reduced-order model for the minimal flow unit": {
        "summary": (
            "Couples a β-VAE-GAN with a sensor-conditioned Easy Attention Transformer "
            "to forecast near-wall turbulence from three point sensors. "
            "Published in Int. J. Heat Fluid Flow."
        ),
        "category": "Near-wall Turbulence",
    },
    "vivaldy a hybrid generative reduced-order model for turbulent flows applied to vortex-induced vibrations": {
        "summary": (
            "Introduces VIVALDy, combining β-VAE-GAN and bidirectional transformer "
            "for reduced-order modelling of VIV systems from cylinder displacement alone. "
            "Published in Physical Review Fluids."
        ),
        "category": "Vortex-Induced Vibrations",
    },
    "vivaldy ai-driven low-order modeling of vortex-induced vibrations": {
        "summary": (
            "Conference precursor to VIVALDy: β-VAE-GAN + transformer framework "
            "for modelling vortex-induced vibrations demonstrated at AiFluids 2025."
        ),
        "category": "Vortex-Induced Vibrations",
    },
    "data-driven modeling of near-wall turbulence using β-variational autoencoder, transformers, and adversarial loss": {
        "summary": (
            "β-VAE-GAN + transformer framework for near-wall turbulence in a minimal "
            "channel at Re_τ=200; predicts latent dynamics within one Lyapunov time. "
            "Presented at THMT-25, Tokyo."
        ),
        "category": "Near-wall Turbulence",
    },
    "simulation of a wingtip vortex flow with linear eddy viscosity turbulence models at re46e6 and re12e6": {
        "summary": (
            "RANS simulation of a wingtip vortex with linear eddy-viscosity models; "
            "compares turbulence closure performance for vortex roll-up prediction."
        ),
        "category": "Computational Fluid Dynamics",
    },
}

FALLBACK_CATEGORY = "Fluid Mechanics"


def normalize_title(title: str) -> str:
    """Lowercase, strip punctuation for dict lookup."""
    return re.sub(r"[^\w\s]", "", title.lower()).strip()


def load_publications() -> list[dict]:
    pubs = []
    for md in sorted(PUBLICATIONS_DIR.glob("*.md")):
        content = md.read_text(encoding="utf-8")
        parts = content.split("---")
        if len(parts) < 3:
            continue
        try:
            meta = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            continue
        abstract_m = re.search(r"## Abstract\n\n(.*?)(\n\n##|\Z)", content, re.DOTALL)
        if abstract_m:
            meta["abstract"] = abstract_m.group(1).strip()
        meta["local_file"] = str(md)
        pubs.append(meta)
    # Sort newest-first by date
    pubs.sort(key=lambda p: str(p.get("date", "")), reverse=True)
    return pubs


# ── Semantic Scholar ───────────────────────────────────────────────────────────

def s2_request(url: str, params: dict):
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, timeout=15)
            if r.status_code == 429:
                print("    S2 rate-limited — waiting 15 s …")
                time.sleep(15)
                continue
            if r.status_code == 200:
                return r.json()
            return None
        except requests.RequestException:
            time.sleep(2)
    return None


def find_s2_paper(title: str, doi: str = ""):
    # DOI lookup is faster and more reliable
    if doi:
        doi_clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
        data = s2_request(f"{S2_API_URL}/paper/DOI:{doi_clean}", {"fields": "paperId"})
        if data and data.get("paperId"):
            return data["paperId"]
    # Fall back to title search
    data = s2_request(
        f"{S2_API_URL}/paper/search",
        {"query": title, "fields": "paperId,title", "limit": 1},
    )
    if data and data.get("data"):
        return data["data"][0]["paperId"]
    return None


def fetch_references(paper_id: str) -> list[dict]:
    data = s2_request(
        f"{S2_API_URL}/paper/{paper_id}/references",
        {"fields": "title,authors,year", "limit": 100},
    )
    if not data:
        return []
    return [r.get("citedPaper", {}) for r in data.get("data", [])]


def is_self_citation(ref: dict) -> bool:
    authors = ref.get("authors") or []
    return any("Tonioni" in (a.get("name") or "") for a in authors)


def calculate_stats(all_refs: list[dict]) -> dict:
    author_counts: Counter = Counter()
    paper_counts: Counter = Counter()
    year_counts: Counter = Counter()

    for ref in all_refs:
        if is_self_citation(ref):
            continue
        for author in ref.get("authors") or []:
            name = author.get("name", "")
            if name:
                # Use "F. Last" format
                parts = name.split()
                short = f"{parts[0][0]}. {parts[-1]}" if len(parts) >= 2 else name
                author_counts[short] += 1
        title = ref.get("title", "")
        year = ref.get("year")
        if title:
            paper_counts[title] += 1
        if year:
            year_counts[int(year)] += 1

    top_authors = [{"name": n, "count": c} for n, c in author_counts.most_common(5)]
    top_papers = [{"title": t, "count": c} for t, c in paper_counts.most_common(5)]
    most_year = year_counts.most_common(1)
    most_influential = (
        {"year": most_year[0][0], "count": most_year[0][1]} if most_year else {}
    )
    return {
        "top_cited_authors": top_authors,
        "top_cited_papers": top_papers,
        "most_influential_year": most_influential,
    }


# ── Embeddings + projection ────────────────────────────────────────────────────

def embed_texts(texts: list[str]) -> np.ndarray:
    print("  Loading sentence-transformer model (all-MiniLM-L6-v2) …")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(texts, show_progress_bar=False)


def project_embeddings(embeddings: np.ndarray) -> list[dict]:
    n = len(embeddings)
    # PCA
    pca = PCA(n_components=2, random_state=42)
    pca_coords = pca.fit_transform(embeddings)

    # UMAP (needs at least 2 samples)
    n_neighbors = max(2, min(n - 1, 15))
    reducer = umap_lib.UMAP(
        n_neighbors=n_neighbors, min_dist=0.3, n_components=2, random_state=42
    )
    umap_coords = reducer.fit_transform(embeddings)

    result = []
    for i in range(n):
        result.append(
            {
                "umap": {"x": round(float(umap_coords[i, 0]), 4), "y": round(float(umap_coords[i, 1]), 4)},
                "pca":  {"x": round(float(pca_coords[i, 0]),  4), "y": round(float(pca_coords[i, 1]),  4)},
            }
        )
    return result


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATS_CACHE.parent.mkdir(parents=True, exist_ok=True)

    # Load stats cache
    stats_cache = {}
    if STATS_CACHE.exists():
        try:
            stats_cache = json.loads(STATS_CACHE.read_text())
        except json.JSONDecodeError:
            pass

    pubs = load_publications()
    print(f"Loaded {len(pubs)} publications.")

    # ── Fetch references from Semantic Scholar ─────────────────────────────────
    all_refs: list[dict] = []
    for pub in pubs:
        title = pub.get("title", "")
        if not title:
            continue
        cache_key = normalize_title(title)
        if cache_key in stats_cache:
            print(f"  [cache] {title[:60]}")
            all_refs.extend(stats_cache[cache_key])
            continue
        doi = str(pub.get("paperurl", ""))
        print(f"  [S2]   {title[:60]}")
        pid = find_s2_paper(title, doi)
        time.sleep(1.1)
        if pid:
            refs = fetch_references(pid)
            time.sleep(1.1)
        else:
            refs = []
            print("         not found on Semantic Scholar")
        stats_cache[cache_key] = refs
        all_refs.extend(refs)

    STATS_CACHE.write_text(json.dumps(stats_cache, indent=2))
    stats = calculate_stats(all_refs)
    print(f"Stats computed. Top author: {stats['top_cited_authors'][0] if stats['top_cited_authors'] else 'n/a'}")

    # ── AI results (summaries + categories) ───────────────────────────────────
    ai_lookup = {normalize_title(k): v for k, v in AI_RESULTS.items()}
    for pub in pubs:
        key = normalize_title(pub.get("title", ""))
        result = ai_lookup.get(key)
        if result:
            pub["ai_results"] = result
        else:
            # Fallback: use abstract or title as summary
            summary = pub.get("abstract", pub.get("title", ""))[:150]
            pub["ai_results"] = {"summary": summary, "category": FALLBACK_CATEGORY}
            print(f"  [warn] no AI result entry for: {pub.get('title','')[:60]}")

    # ── Embeddings ─────────────────────────────────────────────────────────────
    print("Computing embeddings …")
    texts = [
        p["ai_results"]["summary"] + " " + p.get("title", "")
        for p in pubs
    ]
    embeddings = embed_texts(texts)
    coords = project_embeddings(embeddings)

    # ── Assemble output ────────────────────────────────────────────────────────
    output_pubs = []
    for pub, coord in zip(pubs, coords):
        output_pubs.append(
            {
                "title": pub.get("title", ""),
                "date": str(pub.get("date", "")),
                "permalink": pub.get("permalink", ""),
                "pubtype": pub.get("pubtype", ""),
                "map_coords": coord,
                "ai_results": pub["ai_results"],
                "s2_metadata": {"year": str(pub.get("date", ""))[:4]},
            }
        )

    output = {"stats": stats, "publications": output_pubs}
    OUTPUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\nDone. Written to {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

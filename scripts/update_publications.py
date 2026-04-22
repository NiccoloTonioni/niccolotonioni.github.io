# Requirements: pip install scholarly pyyaml google-genai
# Usage:
#   export GEMINI_API_KEY=your_key_here
#   python scripts/update_publications.py

import os
import re
import datetime
import pathlib
import yaml
from scholarly import scholarly
from google import genai

# ── Configuration ──────────────────────────────────────────────────────────────
SCHOLAR_ID = "wTTFZvUAAAAJ&hl"   

GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_SYSTEM_PROMPT = (
    "You are a science communicator writing short, catchy, jargon-light news items "
    "for an academic personal website. Given a paper title and abstract (or just the "
    "title if no abstract), write 2–3 sentences in the third person announcing the work. "
    "Be enthusiastic but precise. Do not use the word \"groundbreaking\"."
)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLICATIONS_DIR = REPO_ROOT / "_publications"
NEWS_FILE = REPO_ROOT / "_data" / "news.yml"
# ──────────────────────────────────────────────────────────────────────────────


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text[:80]  # keep filenames sane


def pub_filename(year: int, title: str) -> pathlib.Path:
    """Return the Path for a publication markdown file."""
    slug = slugify(title)
    date_str = f"{year}-01-01"
    return PUBLICATIONS_DIR / f"{date_str}-{slug}.md"


def existing_titles() -> set[str]:
    """Collect titles already tracked in _publications/."""
    titles = set()
    for md in PUBLICATIONS_DIR.glob("*.md"):
        with md.open() as f:
            content = f.read()
        # extract front-matter block
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if match:
            fm = yaml.safe_load(match.group(1))
            if fm and "title" in fm:
                titles.add(fm["title"].lower().strip())
    return titles


def load_news() -> list[dict]:
    """Load existing news.yml entries (or return empty list)."""
    if NEWS_FILE.exists():
        with NEWS_FILE.open() as f:
            data = yaml.safe_load(f)
        return data if isinstance(data, list) else []
    return []


def save_news(entries: list[dict]) -> None:
    """Write news.yml, sorted newest-first."""
    NEWS_FILE.parent.mkdir(parents=True, exist_ok=True)
    entries_sorted = sorted(entries, key=lambda e: str(e.get("date", "")), reverse=True)
    with NEWS_FILE.open("w") as f:
        yaml.dump(entries_sorted, f, allow_unicode=True, sort_keys=False)


def generate_snippet(title: str, abstract: str | None) -> str:
    """Call Gemini to generate a 2–3 sentence news snippet."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")

    client = genai.Client(api_key=api_key)

    user_text = f"Title: {title}"
    if abstract:
        user_text += f"\n\nAbstract: {abstract}"

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=user_text,
        config=genai.types.GenerateContentConfig(
            system_instruction=GEMINI_SYSTEM_PROMPT,
        ),
    )
    return response.text.strip()


def write_publication(pub_info: dict, snippet: str, ai_generated: bool) -> pathlib.Path:
    """Write a single publication markdown file and return its path."""
    title = pub_info["title"]
    year = pub_info.get("year", datetime.date.today().year)
    authors = pub_info.get("authors", "")
    venue = pub_info.get("venue", "")
    link = pub_info.get("link", "")
    date_str = f"{year}-01-01"

    front_matter = {
        "title": title,
        "authors": authors,
        "venue": venue,
        "year": year,
        "date": date_str,
        "link": link,
        "ai_generated": ai_generated,
    }
    if snippet:
        front_matter["content"] = snippet

    dest = pub_filename(year, title)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w") as f:
        f.write("---\n")
        yaml.dump(front_matter, f, allow_unicode=True, sort_keys=False)
        f.write("---\n")

    return dest


def fetch_publications() -> list[dict]:
    """Fetch all publications for SCHOLAR_ID sorted newest-first."""
    print(f"Fetching Google Scholar profile for ID: {SCHOLAR_ID} …")
    author = scholarly.fill(scholarly.search_author_id(SCHOLAR_ID), sections=["publications"])
    pubs = []
    for pub in author.get("publications", []):
        try:
            filled = scholarly.fill(pub)
        except Exception:
            filled = pub
        bib = filled.get("bib", {})
        pubs.append(
            {
                "title": bib.get("title", "Untitled"),
                "authors": bib.get("author", ""),
                "venue": bib.get("venue", bib.get("journal", bib.get("booktitle", ""))),
                "year": int(bib.get("pub_year", 0)) or datetime.date.today().year,
                "abstract": bib.get("abstract", None),
                "link": filled.get("pub_url", ""),
            }
        )
    pubs.sort(key=lambda p: p["year"], reverse=True)
    return pubs


def main() -> None:
    PUBLICATIONS_DIR.mkdir(parents=True, exist_ok=True)
    known_titles = existing_titles()
    news_entries = load_news()

    publications = fetch_publications()
    new_count = 0

    for pub in publications:
        title_key = pub["title"].lower().strip()
        if title_key in known_titles:
            print(f"  [skip] already exists: {pub['title'][:60]}")
            continue

        print(f"  [new]  {pub['title'][:60]}")
        try:
            snippet = generate_snippet(pub["title"], pub.get("abstract"))
            ai_generated = True
        except Exception as exc:
            print(f"         Gemini call failed ({exc}); saving without snippet.")
            snippet = ""
            ai_generated = False

        pub_path = write_publication(pub, snippet, ai_generated)
        print(f"         → {pub_path.relative_to(REPO_ROOT)}")

        if snippet:
            news_entries.append(
                {
                    "date": f"{pub['year']}-01-01",
                    "title": pub["title"],
                    "snippet": snippet,
                    "link": pub.get("link", ""),
                    "ai_generated": True,
                }
            )

        new_count += 1

    save_news(news_entries)
    print(f"\nDone. {new_count} new publication(s) added; news.yml updated.")


if __name__ == "__main__":
    main()

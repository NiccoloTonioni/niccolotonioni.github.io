#!/bin/bash

# Simple script to bring up the Jekyll server using Docker
# This ensures a consistent environment and automatic refreshing on changes.

echo "Starting Jekyll server at http://localhost:4000..."

docker run --name jekyll-server --rm \
  -v "$(pwd):/srv/jekyll" \
  -e JEKYLL_ENV=development \
  -p 4000:4000 \
  jekyll/jekyll:latest \
  jekyll serve --config _config.yml,_config.dev.yml --force_polling --host 0.0.0.0

#!/bin/bash
# Post-generation hook: download vendor assets and set up the project.

set -e

echo ""
echo "==> Downloading vendor assets (BeerCSS, htmx, Alpine.js)..."
bash scripts/update-vendor.sh

echo ""
echo "==> Installing Python dependencies and generating lock file..."
uv sync

echo ""
echo "Project ready. Next steps:"
echo "  1. cp env.example .env  (and fill in your values)"
echo "  2. ./runlocal.sh"

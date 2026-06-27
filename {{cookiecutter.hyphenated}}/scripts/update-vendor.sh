#!/bin/bash
# Download pinned vendor assets to static/vendor/.
# Run this after project creation and whenever you want to upgrade a dependency.

set -e

VENDOR_DIR="$(dirname "$0")/../static/vendor"
mkdir -p "$VENDOR_DIR"

BEERCSS_VERSION="3.11.11"
HTMX_VERSION="2.0.4"
ALPINE_VERSION="3.14.9"

echo "Downloading BeerCSS ${BEERCSS_VERSION}..."
curl -fsSL "https://cdn.jsdelivr.net/npm/beercss@${BEERCSS_VERSION}/dist/cdn/beer.min.css" -o "${VENDOR_DIR}/beer.min.css"
curl -fsSL "https://cdn.jsdelivr.net/npm/beercss@${BEERCSS_VERSION}/dist/cdn/beer.min.js" -o "${VENDOR_DIR}/beer.min.js"

echo "Downloading htmx ${HTMX_VERSION}..."
curl -fsSL "https://unpkg.com/htmx.org@${HTMX_VERSION}/dist/htmx.min.js" -o "${VENDOR_DIR}/htmx.min.js"

echo "Downloading Alpine.js ${ALPINE_VERSION}..."
curl -fsSL "https://unpkg.com/alpinejs@${ALPINE_VERSION}/dist/cdn.min.js" -o "${VENDOR_DIR}/alpine.min.js"

echo "Done. Vendor assets written to ${VENDOR_DIR}/"
echo ""
echo "Pinned versions:"
echo "  BeerCSS:  ${BEERCSS_VERSION}"
echo "  htmx:     ${HTMX_VERSION}"
echo "  Alpine.js: ${ALPINE_VERSION}"
echo ""
echo "To upgrade, edit the version variables at the top of this script."

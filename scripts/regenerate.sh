#!/bin/bash
set -e

echo "Regenerating client from OpenAPI specification..."

openapi-python-client generate \
  --path openapi.yaml \
  --overwrite

echo "Client regenerated successfully!"
echo "Don't forget to:"
echo "  1. Run tests: pytest"
echo "  2. Update CHANGELOG.md"
echo "  3. Bump version if needed"
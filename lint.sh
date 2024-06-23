#!/bin/bash

echo "Running linter..."

poetry run python -m mypy render_art

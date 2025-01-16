#!/bin/bash

# Get version from the package
VERSION=$(.venv/bin/python -c 'import atlasapprox_disease; print(atlasapprox_disease.__version__)' | tail -n 1)

# Upload to TestPyPI using twine
.venv/bin/twine upload --repository testpypi dist/atlasapprox_disease-${VERSION}* -u __token__ -p $(< testpypi.token)
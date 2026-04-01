"""
A simple script to change the version in pyproject.toml for testing purposes.
"""

import sys
import tomllib
import tomli_w

if len(sys.argv) > 1:
    version = sys.argv[1]
else:
    print("No version provided. Usage: python change-pyproject-version.py <version>")
    exit(1)

with open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)

pyproject["project"]["version"] = version

with open("pyproject.toml", "wb") as f:
    tomli_w.dump(pyproject, f)

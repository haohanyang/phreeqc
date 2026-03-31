#!/bin/bash
set -e

pip install conan ninja
conan profile detect --force

# 1. Clone with sparse initialization
git clone --filter=blob:none --sparse --depth 1 https://github.com/haohanyang/conan-center-index.git
cd conan-center-index

# 2. Set the pattern and explicitly checkout the files
git sparse-checkout set recipes/iphreeqc
git checkout  # Ensures the files are actually pulled into the working tree

# 3. Export the recipe
# We are already inside conan-center-index, so path is relative to here
cd recipes/iphreeqc
conan export all --version 3.8.6

# 4. Return to the project root to install dependencies
# This assumes your project has its own conanfile.txt/py in the root
cd /project 
conan install . --build=missing -s build_type=Release -c tools.cmake.cmaketoolchain:generator=Ninja
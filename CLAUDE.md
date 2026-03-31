Python bindings to IPhreeqc C++ library using pybind11

## Source code

- `src/bindings.cc` Core binding that produces `_phreeqc`
- `src/phreeqc/__init__.py` Python library `phreeqc` that wraps `_phreeqc`
- `src/phreeqc/__init__.pyi` Type hints of editors

## Setup commands

- Run `conan install . --build=missing -s build_type=Debug -c tools.cmake.cmaketoolchain:generator=Ninja` to rebuild cmake toolchain file after conan packages change
- Run `cmake -B build -DCMAKE_BUILD_TYPE=Debug -DCMAKE_TOOLCHAIN_FILE=build/Release/generators/conan_toolchain.cmake` to configure cmake
- Run `cmake --build build --config Debug` to build Python bindings
- See @test_bin.py to properly load and test the python package `phreeqc` in dev environment.

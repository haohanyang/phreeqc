cmake_minimum_required(VERSION 3.20)

project(phreeqc C CXX)

include(FetchContent)

set(CMAKE_CXX_STANDARD 11)

include(ExternalProject)

FetchContent_Declare(
    pybind
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.13.6
    SOURCE_DIR     ${CMAKE_SOURCE_DIR}/pybind11
)

FetchContent_MakeAvailable(pybind)

add_subdirectory(${pybind_SOURCE_DIR})

ExternalProject_Add(IPhreeqcBuild
    URL            https://water.usgs.gov/water-resources/software/PHREEQC/iphreeqc-3.8.6-17100.tar.gz
    CMAKE_ARGS     "-DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR}/iphreeqc-install" "-DBUILD_TESTING=OFF" "-DCMAKE_BUILD_TYPE=Release" "-DCMAKE_POSITION_INDEPENDENT_CODE=ON"
    INSTALL_DIR    "${CMAKE_SOURCE_DIR}/iphreeqc-install"
)


pybind11_add_module(_iphreeqc MODULE "${CMAKE_SOURCE_DIR}/src/bindings.cc")

add_dependencies(_iphreeqc IPhreeqcBuild)

target_link_directories(_iphreeqc 
    PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/lib"
    PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/lib64"
)

target_include_directories(_iphreeqc PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/include")

target_link_libraries(_iphreeqc PRIVATE IPhreeqc)

install(TARGETS _iphreeqc DESTINATION phreeqc)

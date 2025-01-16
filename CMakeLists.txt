cmake_minimum_required(VERSION 3.20)

project(phreeqc)

set(CMAKE_CXX_STANDARD 11)

include(ExternalProject)

add_subdirectory(pybind11)

ExternalProject_Add(IPhreeqcBuild
    SOURCE_DIR     "${CMAKE_SOURCE_DIR}/iphreeqc"
    CMAKE_ARGS     "-DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR}/iphreeqc-install" "-DBUILD_TESTING=OFF" "-DCMAKE_BUILD_TYPE=Release" "-DCMAKE_POSITION_INDEPENDENT_CODE=ON"
    INSTALL_DIR    "${CMAKE_SOURCE_DIR}/iphreeqc-install"
)

pybind11_add_module(_iphreeqc MODULE "${CMAKE_SOURCE_DIR}/src/main.cpp")

add_dependencies(_iphreeqc IPhreeqcBuild)

target_link_directories(_iphreeqc 
    PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/lib"
    PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/lib64"
)

target_include_directories(_iphreeqc PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/include")

target_link_libraries(_iphreeqc PRIVATE IPhreeqc)

install(TARGETS _iphreeqc DESTINATION phreeqc)
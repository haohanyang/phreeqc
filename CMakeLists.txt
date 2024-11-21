cmake_minimum_required(VERSION 3.20)

project(phreeqc)

add_subdirectory(pybind11)

include(ExternalProject)

ExternalProject_Add(IPhreeqcBuild
    GIT_REPOSITORY https://github.com/usgs-coupled/iphreeqc.git
    GIT_TAG        v3.8.3
    CMAKE_ARGS     "-DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR}/iphreeqc-install" "-DBUILD_TESTING=OFF" "-DCMAKE_BUILD_TYPE=Release"
    INSTALL_DIR    "${CMAKE_SOURCE_DIR}/iphreeqc-install"
)


pybind11_add_module(_iphreeqc MODULE "${CMAKE_SOURCE_DIR}/src/main.cpp")

add_dependencies(_iphreeqc IPhreeqcBuild)

target_link_directories(_iphreeqc PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/lib")

target_include_directories(_iphreeqc PRIVATE "${CMAKE_SOURCE_DIR}/iphreeqc-install/include")

target_link_libraries(_iphreeqc PRIVATE IPhreeqc)

install(TARGETS _iphreeqc DESTINATION phreeqc)
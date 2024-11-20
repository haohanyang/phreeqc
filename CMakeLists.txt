cmake_minimum_required(VERSION 3.20)

project(phreeqc)

add_subdirectory(pybind11)

pybind11_add_module(_iphreeqc MODULE "src/main.cpp")

target_link_directories(_iphreeqc PRIVATE "iphreeqc-install/lib")

target_include_directories(_iphreeqc PRIVATE "iphreeqc-install/include")

target_link_libraries(_iphreeqc PRIVATE IPhreeqc)

install(TARGETS _iphreeqc DESTINATION phreeqc)

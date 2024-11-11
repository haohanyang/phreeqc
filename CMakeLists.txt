cmake_minimum_required(VERSION 3.15)

project (
  phreeqc
  VERSION 3.6.3
  LANGUAGES CXX
  )

set(MODULE_NAME _phreeqc)
set(LIB_TYPE STATIC)
add_subdirectory(pybind11)
add_subdirectory(iphreeqc)
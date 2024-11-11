cmake_minimum_required(VERSION 3.15)

project (
  phreeqc
  VERSION 3.6.3
  LANGUAGES C CXX
  )

add_subdirectory(pybind11)
add_subdirectory(iphreeqc)
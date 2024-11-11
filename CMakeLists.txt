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

pybind11_add_module(${MODULE_NAME} SHARED src/main.cpp)

target_link_libraries(${MODULE_NAME} PRIVATE IPhreeqc)

install(TARGETS ${MODULE_NAME} DESTINATION phreeqc)

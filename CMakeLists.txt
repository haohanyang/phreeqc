cmake_minimum_required(VERSION 3.20)

project(phreeqc C CXX)

set(CMAKE_CXX_STANDARD 11)

find_package(IPhreeqc REQUIRED CONFIG)

find_package(pybind11 REQUIRED)

pybind11_add_module(phreeqc MODULE ${CMAKE_SOURCE_DIR}/src/bindings.cc)

target_link_libraries(phreeqc PRIVATE IPhreeqc::IPhreeqc)

install(TARGETS phreeqc DESTINATION phreeqc)

add_custom_command(TARGET phreeqc POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E echo "------------------------------------------------------"
    COMMAND ${CMAKE_COMMAND} -E echo "Binary Location: $<TARGET_FILE:phreeqc>"
    COMMAND ${CMAKE_COMMAND} -E echo "------------------------------------------------------"
)
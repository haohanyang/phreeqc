cmake_minimum_required(VERSION 3.20)

project(phreeqc C CXX)

set(CMAKE_CXX_STANDARD 17)

find_package(IPhreeqc REQUIRED CONFIG)

find_package(pybind11 REQUIRED)

message(STATUS "Found Python version: ${PYTHON_VERSION}")
message(STATUS "Python Include Dir: ${PYTHON_INCLUDE_DIRS}")
message(STATUS "Python Executable: ${PYTHON_EXECUTABLE}")

pybind11_add_module(_phreeqc MODULE ${CMAKE_SOURCE_DIR}/src/bindings.cc)

target_link_libraries(_phreeqc PRIVATE IPhreeqc::IPhreeqc)

install(TARGETS _phreeqc DESTINATION phreeqc)

install(DIRECTORY "${CMAKE_SOURCE_DIR}/src/phreeqc/databases/"
    DESTINATION "phreeqc/databases"
    FILES_MATCHING PATTERN "*.dat"
)

set(PYTHON_PKG_DIR "${CMAKE_SOURCE_DIR}/src/phreeqc")

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_custom_command(TARGET _phreeqc POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E make_directory "${PYTHON_PKG_DIR}"
        COMMAND ${CMAKE_COMMAND} -E copy "$<TARGET_FILE:_phreeqc>" "${PYTHON_PKG_DIR}/"
        COMMENT "Copying extension to ${PYTHON_PKG_DIR}"
    )
endif()
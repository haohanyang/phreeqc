# CMAKE_MSVC_RUNTIME_LIBRARY requires 3.15
cmake_minimum_required(VERSION 3.15)

project (
  phreeqc
  VERSION 3.8.3
  LANGUAGES CXX C
  )

set(STANDALONE_BUILD 0)

if (STANDALONE_BUILD)
  # Set a default build type if none was specified
  set(default_build_type "Release")
  if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE "${default_build_type}" CACHE
      STRING "Choose the type of build." FORCE)
    # Set the possible values of build type for cmake-gui
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS
      "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
  endif()
endif()

# overide docdir on windows
if (WIN32 AND NOT CMAKE_INSTALL_DOCDIR)
  set(CMAKE_INSTALL_DOCDIR "" CACHE PATH "documentation root (doc)")
  set(CMAKE_INSTALL_DOCDIR "doc")
endif()

# set standard directory locations
include(GNUInstallDirs)

if (STANDALONE_BUILD AND MSVC)
  option (IPHREEQC_STATIC_RUNTIME "Build with a static runtime" OFF)
  if (IPHREEQC_STATIC_RUNTIME)
    # compile with static runtime
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
  endif()
endif()

# Fortran
option (IPHREEQC_ENABLE_MODULE "Enable Fortran module" ON)
if (STANDALONE_BUILD)
  if (IPHREEQC_FORTRAN_TESTING)
    enable_language(Fortran)
  else()
    if (CMAKE_Fortran_COMPILER)
      option (IPHREEQC_FORTRAN_TESTING "Build Fortran test" ON)
    else()
      option (IPHREEQC_FORTRAN_TESTING "Build Fortran test" OFF)
    endif()
  endif()
endif()

# compile Var.c as c++
set_source_files_properties(iphreeqc/src/Var.c PROPERTIES LANGUAGE CXX)

if (STANDALONE_BUILD)
  option(BUILD_SHARED_LIBS "Build Shared Libraries" OFF)
  set(LIB_TYPE STATIC)
endif()

if (STANDALONE_BUILD)
  if (MSVC)
    option(BUILD_CLR_LIBS "Build CLR Libraries" OFF)
  endif()
endif()

if (BUILD_SHARED_LIBS)
  set(LIB_TYPE SHARED)
endif()

add_subdirectory(pybind11)

pybind11_add_module(IPhreeqc ${LIB_TYPE} src/main.cpp)

target_sources(IPhreeqc
  PRIVATE
    iphreeqc/src/IPhreeqc.cpp
    iphreeqc/src/CSelectedOutput.cpp
    iphreeqc/src/CSelectedOutput.hxx
    iphreeqc/src/CVar.hxx
    iphreeqc/src/Debug.h
    iphreeqc/src/ErrorReporter.hxx
    iphreeqc/src/IPhreeqc.h
    iphreeqc/src/IPhreeqc.hpp
    iphreeqc/src/IPhreeqc_interface_F.cpp
    iphreeqc/src/IPhreeqcCallbacks.h
    iphreeqc/src/IPhreeqcLib.cpp
    iphreeqc/src/phreeqcpp/advection.cpp
    iphreeqc/src/phreeqcpp/basicsubs.cpp
    iphreeqc/src/phreeqcpp/cl1.cpp
    iphreeqc/src/phreeqcpp/common/Parser.cxx
    iphreeqc/src/phreeqcpp/common/Parser.h
    iphreeqc/src/phreeqcpp/common/PHRQ_base.cxx
    iphreeqc/src/phreeqcpp/common/PHRQ_base.h
    iphreeqc/src/phreeqcpp/common/PHRQ_exports.h
    iphreeqc/src/phreeqcpp/common/PHRQ_io.cpp
    iphreeqc/src/phreeqcpp/common/PHRQ_io.h
    iphreeqc/src/phreeqcpp/common/phrqtype.h
    iphreeqc/src/phreeqcpp/common/Utils.cxx
    iphreeqc/src/phreeqcpp/common/Utils.h
    iphreeqc/src/phreeqcpp/cvdense.cpp
    iphreeqc/src/phreeqcpp/cvdense.h
    iphreeqc/src/phreeqcpp/cvode.cpp
    iphreeqc/src/phreeqcpp/cvode.h
    iphreeqc/src/phreeqcpp/cxxKinetics.cxx
    iphreeqc/src/phreeqcpp/cxxKinetics.h
    iphreeqc/src/phreeqcpp/cxxMix.cxx
    iphreeqc/src/phreeqcpp/cxxMix.h
    iphreeqc/src/phreeqcpp/dense.cpp
    iphreeqc/src/phreeqcpp/dense.h
    iphreeqc/src/phreeqcpp/Dictionary.cpp
    iphreeqc/src/phreeqcpp/Dictionary.h
    iphreeqc/src/phreeqcpp/dumper.cpp
    iphreeqc/src/phreeqcpp/dumper.h
    iphreeqc/src/phreeqcpp/Exchange.cxx
    iphreeqc/src/phreeqcpp/Exchange.h
    iphreeqc/src/phreeqcpp/ExchComp.cxx
    iphreeqc/src/phreeqcpp/ExchComp.h
    iphreeqc/src/phreeqcpp/GasComp.cxx
    iphreeqc/src/phreeqcpp/GasComp.h
    iphreeqc/src/phreeqcpp/gases.cpp
    iphreeqc/src/phreeqcpp/GasPhase.cxx
    iphreeqc/src/phreeqcpp/GasPhase.h
    iphreeqc/src/phreeqcpp/global_structures.h
    iphreeqc/src/phreeqcpp/input.cpp
    iphreeqc/src/phreeqcpp/integrate.cpp
    iphreeqc/src/phreeqcpp/inverse.cpp
    iphreeqc/src/phreeqcpp/ISolution.cxx
    iphreeqc/src/phreeqcpp/ISolution.h
    iphreeqc/src/phreeqcpp/ISolutionComp.cxx
    iphreeqc/src/phreeqcpp/ISolutionComp.h
    iphreeqc/src/phreeqcpp/isotopes.cpp
    iphreeqc/src/phreeqcpp/kinetics.cpp
    iphreeqc/src/phreeqcpp/KineticsComp.cxx
    iphreeqc/src/phreeqcpp/KineticsComp.h
    iphreeqc/src/phreeqcpp/mainsubs.cpp
    iphreeqc/src/phreeqcpp/model.cpp
    iphreeqc/src/phreeqcpp/NA.h
    iphreeqc/src/phreeqcpp/NameDouble.cxx
    iphreeqc/src/phreeqcpp/NameDouble.h
    iphreeqc/src/phreeqcpp/NumKeyword.cxx
    iphreeqc/src/phreeqcpp/NumKeyword.h
    iphreeqc/src/phreeqcpp/nvector.cpp
    iphreeqc/src/phreeqcpp/nvector.h
    iphreeqc/src/phreeqcpp/nvector_serial.cpp
    iphreeqc/src/phreeqcpp/nvector_serial.h
    iphreeqc/src/phreeqcpp/parse.cpp
    iphreeqc/src/phreeqcpp/PBasic.cpp
    iphreeqc/src/phreeqcpp/PBasic.h
    iphreeqc/src/phreeqcpp/phqalloc.cpp
    iphreeqc/src/phreeqcpp/phqalloc.h
    iphreeqc/src/phreeqcpp/Phreeqc.cpp
    iphreeqc/src/phreeqcpp/Phreeqc.h
    iphreeqc/src/phreeqcpp/PhreeqcKeywords/Keywords.cpp
    iphreeqc/src/phreeqcpp/PhreeqcKeywords/Keywords.h
    iphreeqc/src/phreeqcpp/PHRQ_io_output.cpp
    iphreeqc/src/phreeqcpp/pitzer.cpp
    iphreeqc/src/phreeqcpp/pitzer_structures.cpp
    iphreeqc/src/phreeqcpp/PPassemblage.cxx
    iphreeqc/src/phreeqcpp/PPassemblage.h
    iphreeqc/src/phreeqcpp/PPassemblageComp.cxx
    iphreeqc/src/phreeqcpp/PPassemblageComp.h
    iphreeqc/src/phreeqcpp/prep.cpp
    iphreeqc/src/phreeqcpp/Pressure.cxx
    iphreeqc/src/phreeqcpp/Pressure.h
    iphreeqc/src/phreeqcpp/print.cpp
    iphreeqc/src/phreeqcpp/Reaction.cxx
    iphreeqc/src/phreeqcpp/Reaction.h
    iphreeqc/src/phreeqcpp/read.cpp
    iphreeqc/src/phreeqcpp/ReadClass.cxx
    iphreeqc/src/phreeqcpp/readtr.cpp
    iphreeqc/src/phreeqcpp/runner.cpp
    iphreeqc/src/phreeqcpp/runner.h
    iphreeqc/src/phreeqcpp/SelectedOutput.cpp
    iphreeqc/src/phreeqcpp/SelectedOutput.h
    iphreeqc/src/phreeqcpp/Serializer.cxx
    iphreeqc/src/phreeqcpp/Serializer.h
    iphreeqc/src/phreeqcpp/sit.cpp
    iphreeqc/src/phreeqcpp/smalldense.cpp
    iphreeqc/src/phreeqcpp/smalldense.h
    iphreeqc/src/phreeqcpp/Solution.cxx
    iphreeqc/src/phreeqcpp/Solution.h
    iphreeqc/src/phreeqcpp/SolutionIsotope.cxx
    iphreeqc/src/phreeqcpp/SolutionIsotope.h
    iphreeqc/src/phreeqcpp/spread.cpp
    iphreeqc/src/phreeqcpp/SS.cxx
    iphreeqc/src/phreeqcpp/SS.h
    iphreeqc/src/phreeqcpp/SSassemblage.cxx
    iphreeqc/src/phreeqcpp/SSassemblage.h
    iphreeqc/src/phreeqcpp/SScomp.cxx
    iphreeqc/src/phreeqcpp/SScomp.h
    iphreeqc/src/phreeqcpp/step.cpp
    iphreeqc/src/phreeqcpp/StorageBin.cxx
    iphreeqc/src/phreeqcpp/StorageBin.h
    iphreeqc/src/phreeqcpp/StorageBinList.cpp
    iphreeqc/src/phreeqcpp/StorageBinList.h
    iphreeqc/src/phreeqcpp/structures.cpp
    iphreeqc/src/phreeqcpp/sundialsmath.cpp
    iphreeqc/src/phreeqcpp/sundialsmath.h
    iphreeqc/src/phreeqcpp/sundialstypes.h
    iphreeqc/src/phreeqcpp/Surface.cxx
    iphreeqc/src/phreeqcpp/Surface.h
    iphreeqc/src/phreeqcpp/SurfaceCharge.cxx
    iphreeqc/src/phreeqcpp/SurfaceCharge.h
    iphreeqc/src/phreeqcpp/SurfaceComp.cxx
    iphreeqc/src/phreeqcpp/SurfaceComp.h
    iphreeqc/src/phreeqcpp/System.cxx
    iphreeqc/src/phreeqcpp/System.h
    iphreeqc/src/phreeqcpp/tally.cpp
    iphreeqc/src/phreeqcpp/Temperature.cxx
    iphreeqc/src/phreeqcpp/Temperature.h
    iphreeqc/src/phreeqcpp/tidy.cpp
    iphreeqc/src/phreeqcpp/transport.cpp
    iphreeqc/src/phreeqcpp/Use.cpp
    iphreeqc/src/phreeqcpp/Use.h
    iphreeqc/src/phreeqcpp/UserPunch.cpp
    iphreeqc/src/phreeqcpp/UserPunch.h
    iphreeqc/src/phreeqcpp/utilities.cpp
    iphreeqc/src/thread.h
    iphreeqc/src/Var.c
    iphreeqc/src/Var.h
    iphreeqc/src/Version.h
)

target_include_directories(IPhreeqc
  PUBLIC
    iphreeqc/src
    iphreeqc/src/phreeqcpp
    iphreeqc/src/phreeqcpp/common
    iphreeqc/src/phreeqcpp/PhreeqcKeywords
  )

target_compile_definitions(IPhreeqc PRIVATE SWIG_SHARED_OBJ)
target_compile_definitions(IPhreeqc PRIVATE USE_PHRQ_ALLOC)

if (NOT IPHREEQC_ENABLE_MODULE)
  target_compile_definitions(IPhreeqc
    PUBLIC
      IPHREEQC_NO_FORTRAN_MODULE
  )

  target_sources(IPhreeqc
    PRIVATE
      iphreeqc/src/fimpl.h
      iphreeqc/src/fwrap.cpp
      iphreeqc/src/fwrap1.cpp
      iphreeqc/src/fwrap2.cpp
      iphreeqc/src/fwrap3.cpp
      iphreeqc/src/fwrap4.cpp
      iphreeqc/src/fwrap5.cpp
      iphreeqc/src/fwrap6.cpp
      iphreeqc/src/fwrap7.cpp
      iphreeqc/src/fwrap8.cpp
  )
endif()

if (${CMAKE_CXX_COMPILER_ID} STREQUAL MSVC)
  target_compile_options(IPhreeqc PRIVATE /wd4251 /wd4275 /wd4793)
endif()

# Disable deprecation warnings for standard C and STL functions in VS2005
# and later
if (MSVC_VERSION EQUAL 1400 OR MSVC_VERSION GREATER 1400)
  target_compile_definitions(IPhreeqc PUBLIC _CRT_SECURE_NO_DEPRECATE)
  target_compile_definitions(IPhreeqc PUBLIC _SCL_SECURE_NO_WARNINGS)
endif()

if (WIN32 AND BUILD_SHARED_LIBS)
  # Required to build IMPLIB
  # (Seems to be automatically set when using Visual Studio as the generator)
  target_compile_definitions(IPhreeqc PRIVATE _WINDLL)
endif()

# Allow user to override POSTFIX properties (but mandate them so that
# all builds can be installed to the same directory)
if (NOT CMAKE_DEBUG_POSTFIX)
  set_target_properties(IPhreeqc PROPERTIES DEBUG_POSTFIX "d")
endif()

if (NOT CMAKE_MINSIZEREL_POSTFIX)
  set_target_properties(IPhreeqc PROPERTIES MINSIZEREL_POSTFIX "msr")
endif()

if (NOT CMAKE_RELWITHDEBINFO_POSTFIX)
  set_target_properties(IPhreeqc PROPERTIES RELWITHDEBINFO_POSTFIX "rwd")
endif()

set(IPhreeqc_Headers
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqc.h
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqc.hpp
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqcCallbacks.h
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/phreeqcpp/PhreeqcKeywords/Keywords.h
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/phreeqcpp/common/PHRQ_exports.h
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/phreeqcpp/common/PHRQ_io.h
  ${PROJECT_SOURCE_DIR}/iphreeqc/src/Var.h
  )

if (IPHREEQC_ENABLE_MODULE)
  set(IPhreeqc_SRC
    ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqc_interface.F90
    ${PROJECT_SOURCE_DIR}/iphreeqc/src/README.Fortran
    )
else()
  # always install README.Fortran
  set(IPhreeqc_SRC
    ${PROJECT_SOURCE_DIR}/iphreeqc/src/README.Fortran
    )
  # install old fortran include files
  set(IPhreeqc_Headers
    ${IPhreeqc_Headers}
    ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqc.f.inc
    ${PROJECT_SOURCE_DIR}/iphreeqc/src/IPhreeqc.f90.inc
    )
endif()

# Setup references for /CLR
if (MSVC AND BUILD_SHARED_LIBS AND BUILD_CLR_LIBS)
  if (MSVC_VERSION LESS 1600)
    message(FATAL_ERROR "CLR options must be set manually for versions prior to Visual Studio 2010")
  endif()
  set_target_properties(IPhreeqc PROPERTIES VS_DOTNET_REFERENCES "System;System.Drawing;System.Windows.Forms;${CMAKE_CURRENT_SOURCE_DIR}/iphreeqc/src/phreeqcpp/ZedGraph.dll")
  set_target_properties(IPhreeqc PROPERTIES COMMON_LANGUAGE_RUNTIME "")
  target_compile_definitions(IPhreeqc PRIVATE "MULTICHART")
endif()

set_target_properties(IPhreeqc PROPERTIES
  VERSION "${IPhreeqc_VERSION}"
  SOVERSION "${IPhreeqc_VERSION_MAJOR}"
  )

# install
if (STANDALONE_BUILD)

  include(CMakePackageConfigHelpers)

  configure_package_config_file(IPhreeqcConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/IPhreeqcConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/IPhreeqc
    )

  write_basic_package_version_file("IPhreeqcConfigVersion.cmake"
    VERSION ${IPhreeqc_VERSION}
    COMPATIBILITY SameMajorVersion
    )

  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/IPhreeqcConfig.cmake ${CMAKE_CURRENT_BINARY_DIR}/IPhreeqcConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/IPhreeqc
    )

  install(TARGETS  IPhreeqc
    EXPORT   IPhreeqcTargets
    LIBRARY  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME  DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    )
  install(EXPORT IPhreeqcTargets
    FILE IPhreeqcTargets.cmake
    NAMESPACE IPhreeqc::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/IPhreeqc
    )

  install(FILES ${IPhreeqc_Headers} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
  if (WIN32)
    install(FILES ${IPhreeqc_SRC} DESTINATION src)
  else()
    install(FILES ${IPhreeqc_SRC} DESTINATION ${CMAKE_INSTALL_DOCDIR}/src)
  endif()
  if (BUILD_CLR_LIBS)
    install(FILES "${PROJECT_SOURCE_DIR}/iphreeqc/src/phreeqcpp/ZedGraph.dll" DESTINATION ${CMAKE_INSTALL_BINDIR})
  endif()
endif()

if (BUILD_CLR_LIBS)
  if (NOT BUILD_SHARED_LIBS)
    message(FATAL_ERROR "BUILD_CLR_LIBS requires that BUILD_SHARED_LIBS be set")
  endif()

  if (IPHREEQC_STATIC_RUNTIME)
    message(FATAL_ERROR "BUILD_CLR_LIBS and IPHREEQC_STATIC_RUNTIME are mutually exclusive")
  endif()

  # CLR files
  target_sources(IPhreeqc
    PRIVATE
      iphreeqc/src/phreeqcpp/ChartHandler.cpp
      iphreeqc/src/phreeqcpp/ChartHandler.h
      iphreeqc/src/phreeqcpp/ChartObject.cpp
      iphreeqc/src/phreeqcpp/ChartObject.h
      iphreeqc/src/phreeqcpp/CurveObject.cpp
      iphreeqc/src/phreeqcpp/CurveObject.h
  )

endif()

include (CTest)

if (STANDALONE_BUILD)

  add_subdirectory(database)
  add_subdirectory(doc)
  add_subdirectory(examples)

  if (BUILD_TESTING)
    add_subdirectory(tests)
  endif()


  if (BUILD_TESTING)  # may need to add MSVC version check
    include(FetchContent)

    # Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP in CMake 3.24:
    if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
      cmake_policy(SET CMP0135 NEW)
    endif()    

    FetchContent_Declare(
      googletest
      URL https://github.com/google/googletest/archive/release-1.12.1.tar.gz
      )

    mark_as_advanced(
      FETCHCONTENT_BASE_DIR
      FETCHCONTENT_FULLY_DISCONNECTED
      FETCHCONTENT_QUIET
      FETCHCONTENT_SOURCE_DIR_GOOGLETEST
      FETCHCONTENT_UPDATES_DISCONNECTED
      FETCHCONTENT_UPDATES_DISCONNECTED_GOOGLETEST
      )

    # Prevent GoogleTest from overriding our compiler/linker options
    # when building with Visual Studio
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

    set(BUILD_GTEST ON CACHE BOOL "" FORCE)
    set(BUILD_GMOCK ON CACHE BOOL "" FORCE)

    set(INSTALL_GTEST OFF CACHE BOOL "" FORCE)
    set(INSTALL_GMOCK OFF CACHE BOOL "" FORCE)

    mark_as_advanced(
      BUILD_GTEST
      BUILD_GMOCK
      INSTALL_GTEST
      INSTALL_GMOCK
      gmock_build_tests
      gtest_build_tests
      gtest_build_samples
      gtest_disable_pthreads
      gtest_force_shared_crt
      gtest_hide_internal_symbols
      )

    FetchContent_GetProperties(googletest)
    if (NOT googletest_POPULATED)
      # Always build googletest static
      set(SAVE_BUILD_SHARED_LIBS ${BUILD_SHARED_LIBS})
      set(BUILD_SHARED_LIBS OFF)
      FetchContent_MakeAvailable(googletest)
      set(BUILD_SHARED_LIBS ${SAVE_BUILD_SHARED_LIBS})
    endif()

    add_subdirectory(gtest)
  endif()
endif()


install(TARGETS IPhreeqc DESTINATION phreeqc)
# /CMakeLists.txt
#
# Main build file for cmake-forward-arguments
#
# See /LICENCE.md for Copyright information
project (CMakeForwardArguments)
cmake_minimum_required (VERSION 2.8 FATAL_ERROR)

include ("${CMAKE_CURRENT_LIST_DIR}/conanbuildinfo.cmake")
conan_basic_setup ()

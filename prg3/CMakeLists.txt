# cmake_minimum_required(VERSION <specify CMake version here>)
project(prg3)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(prg3
        Biob.h
        Csci.h
        Egen.h
        main.cpp
        Semester.h
        University.h)

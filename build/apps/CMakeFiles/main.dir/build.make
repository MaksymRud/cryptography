# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\msys64\mingw64\bin\cmake.exe

# The command to remove a file.
RM = C:\msys64\mingw64\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Code\python\Lab1Cript\Lab2\FastCLib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Code\python\Lab1Cript\Lab2\build

# Include any dependencies generated for this target.
include apps/CMakeFiles/main.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include apps/CMakeFiles/main.dir/compiler_depend.make

# Include the progress variables for this target.
include apps/CMakeFiles/main.dir/progress.make

# Include the compile flags for this target's objects.
include apps/CMakeFiles/main.dir/flags.make

apps/CMakeFiles/main.dir/main.cpp.obj: apps/CMakeFiles/main.dir/flags.make
apps/CMakeFiles/main.dir/main.cpp.obj: apps/CMakeFiles/main.dir/includes_CXX.rsp
apps/CMakeFiles/main.dir/main.cpp.obj: D:/Code/python/Lab1Cript/Lab2/FastCLib/apps/main.cpp
apps/CMakeFiles/main.dir/main.cpp.obj: apps/CMakeFiles/main.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Code\python\Lab1Cript\Lab2\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object apps/CMakeFiles/main.dir/main.cpp.obj"
	cd /d D:\Code\python\Lab1Cript\Lab2\build\apps && C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT apps/CMakeFiles/main.dir/main.cpp.obj -MF CMakeFiles\main.dir\main.cpp.obj.d -o CMakeFiles\main.dir\main.cpp.obj -c D:\Code\python\Lab1Cript\Lab2\FastCLib\apps\main.cpp

apps/CMakeFiles/main.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/main.dir/main.cpp.i"
	cd /d D:\Code\python\Lab1Cript\Lab2\build\apps && C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Code\python\Lab1Cript\Lab2\FastCLib\apps\main.cpp > CMakeFiles\main.dir\main.cpp.i

apps/CMakeFiles/main.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/main.dir/main.cpp.s"
	cd /d D:\Code\python\Lab1Cript\Lab2\build\apps && C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Code\python\Lab1Cript\Lab2\FastCLib\apps\main.cpp -o CMakeFiles\main.dir\main.cpp.s

# Object files for target main
main_OBJECTS = \
"CMakeFiles/main.dir/main.cpp.obj"

# External object files for target main
main_EXTERNAL_OBJECTS =

apps/main.exe: apps/CMakeFiles/main.dir/main.cpp.obj
apps/main.exe: apps/CMakeFiles/main.dir/build.make
apps/main.exe: fast/libfast.dll.a
apps/main.exe: apps/CMakeFiles/main.dir/linklibs.rsp
apps/main.exe: apps/CMakeFiles/main.dir/objects1.rsp
apps/main.exe: apps/CMakeFiles/main.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Code\python\Lab1Cript\Lab2\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable main.exe"
	cd /d D:\Code\python\Lab1Cript\Lab2\build\apps && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\main.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
apps/CMakeFiles/main.dir/build: apps/main.exe
.PHONY : apps/CMakeFiles/main.dir/build

apps/CMakeFiles/main.dir/clean:
	cd /d D:\Code\python\Lab1Cript\Lab2\build\apps && $(CMAKE_COMMAND) -P CMakeFiles\main.dir\cmake_clean.cmake
.PHONY : apps/CMakeFiles/main.dir/clean

apps/CMakeFiles/main.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Code\python\Lab1Cript\Lab2\FastCLib D:\Code\python\Lab1Cript\Lab2\FastCLib\apps D:\Code\python\Lab1Cript\Lab2\build D:\Code\python\Lab1Cript\Lab2\build\apps D:\Code\python\Lab1Cript\Lab2\build\apps\CMakeFiles\main.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : apps/CMakeFiles/main.dir/depend


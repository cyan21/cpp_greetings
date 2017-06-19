from conans import ConanFile, CMake, tools
import os


class GreetingsConan(ConanFile):
    name = "Greetings"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    # reference sources in the current folder
    # COMMENT OUT if you want to fetch source from GITHUB
    exports_sources = "./*"

    def source(self):
        # UNCOMMENT if you want to fetch source from GITHUB 
#       self.run("git clone https://github.com/cyan21/cpp_greetings.git")
#       self.run("cd cpp_greetings && git checkout conan_deps")

        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        # UNCOMMENT if you want to fetch source from GITHUB 
#       tools.replace_in_file("cpp_greetings/CMakeLists.txt", "PROJECT(myGreetings)", '''PROJECT(myGreetings)

        # COMMENT OUT when using source from GITHUB
        tools.replace_in_file("./CMakeLists.txt", "PROJECT(myGreetings)", '''PROJECT(myGreetings)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        # UNCOMMENT if you want to fetch source from GITHUB 
#        self.run('cmake cpp_greetings %s %s' % (cmake.command_line, shared))

        # COMMENT OUT when using source from GITHUB
        self.run('cmake . %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        # UNCOMMENT if you want to fetch source from GITHUB 
#        self.copy("*.h", dst="include", src="cpp_greetings")
        self.copy("*.h", dst="include", src=".")

        # see CMakeLists.txt to get the name of the lib ==> ADD_LIBRARY  
        self.copy("*greet.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["greet"]

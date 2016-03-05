from conans import ConanFile
from conans.tools import download, unzip
import os


class CMakeForwardArgumentsConan(ConanFile):
    name = "cmake-forward-arguments"
    version = "master"
    generators = "cmake"
    requires = ("cmake-include-guard/master@smspillaz/cmake-include-guard", )
    url = "http://github.com/polysquare/cmake-forward-arguments"
    license = "MIT"

    def source(self):
        zip_name = "cmake-forward-arguments-master.zip"
        download("https://github.com/polysquare/" +
                 "cmake-forward-arguments/archive/master.zip", zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-forward-arguments",
                  src=".",
                  keep_path=True)

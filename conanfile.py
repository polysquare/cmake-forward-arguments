from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.3"


class CMakeForwardArguments(ConanFile):
    name = "cmake-forward-arguments"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    requires = ("cmake-include-guard/master@smspillaz/cmake-include-guard",
                "cmake-module-common/master@smspillaz/cmake-module-common")
    generators = "cmake"
    url = "http://github.com/polysquare/cmake-forward-arguments"
    licence = "MIT"
    options = {
        "dev": [True, False]
    }
    default_options = "dev=False"

    def requirements(self):
        if self.options.dev:
            self.requires("cmake-module-common/master@smspillaz/cmake-module-common")

    def source(self):
        zip_name = "cmake-forward-arguments.zip"
        download("https://github.com/polysquare/"
                 "cmake-forward-arguments/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-forward-arguments",
                  src="cmake-forward-arguments-" + VERSION,
                  keep_path=True)

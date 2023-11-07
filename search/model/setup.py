from setuptools import setup
from Cython.Build import cythonize

setup(
    package_dir={'model': ''},
    ext_modules = cythonize("State_C1.pyx")
)
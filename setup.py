#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="Package for parsing DOI from PPT",
    version="0.1.dev0",
    url="https://github.com/ceebios/ceebios_parser",
    author="Nikolay Tchakarov",
    license="License :: OSI Approved :: Apache Software License",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.txt").readlines(),
    description="Parse DOIS from PPT and return articles meta data",
    long_description="\n" + open("README.md").read(),
)

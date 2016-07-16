#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="ACCUConfWeb",
    version="0.1",
    packages=find_packages('accuconf'),
    install_requires=[
        "Flask=0.11",
        "Flask-SQLAlchemy=2.1",
        "SQLAlchemy=1.0.1",
        "pytest-runner"
    ],
    test_requires=[
        "pytest"
    ],
    package_data={
        '': ['*.txt', '*.adoc', '*.json']
    },
    package_dir={'': 'accuconf'},
    author="ACCUConf",
    url="https://github.com/benignbala/accuconfweb"
)

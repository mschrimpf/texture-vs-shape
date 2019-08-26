#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "torch",
    "torchvision",
]

setup(
    name='texture-vs-shape',
    version='0.1.0',
    description=readme,
    long_description=readme,
    packages=['texture_vs_shape'],
    install_requires=requirements,
)

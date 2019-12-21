#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='region-calc',
    author='n4sr',
    url='https://github.com/n4sr/region-calc',
    version='0.1.1',
    license='GPL3.0',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'region-calc=regioncalc.__main__:run'
        ]
    }
)
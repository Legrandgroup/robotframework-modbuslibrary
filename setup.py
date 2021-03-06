#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for Modbus Robotframework library"""

from __future__ import with_statement
from setuptools import setup
from os.path import abspath, dirname, join

from rfmodbuslib import __lib_version__

def read(fname):
    """read and return fname file content"""
    curdir = dirname(abspath(__file__))
    with open(join(curdir, fname)) as filename:
        return filename.read()

CLASSIFIERS = """
Development Status :: 3 - Alpha
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-modbuslibrary',
    version=__lib_version__,
    description='Robot Framework library for Modbus',
    long_description=read('README.rst'),
    author='Legrand Developers (SWAT team)',
    author_email='pierre.roth@legrand.fr',
    url='https://github.com/Legrandgroup/robotframework-modbuslibrary',
    license='Apache License 2.0',
    keywords='robotframework testing testautomation modbus',
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    packages=['rfmodbuslib'],
    install_requires=['robotframework', 'modbus_tk', 'pyserial'],
    extras_require = {
        'Sphynx': ["sphynx"],
    }
)

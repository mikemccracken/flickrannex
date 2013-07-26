#! /usr/bin/env python2

from setuptools import setup, find_packages

setup(
    name = 'flickrannex',
    version = '0.0',
    scripts = ['flickrannex.py'],
    packages = ['lib'],
    package_data = {
        'lib' : ['logo_small.png'],
        }
    )

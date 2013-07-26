#! /usr/bin/env python2

from setuptools import setup, find_packages

setup(
    name = 'flickrannex',
    version = '0.0',
    scripts = ['flickrannex'],
    packages = ['libflickrannex'],
    package_data = {
        'libflickrannex' : ['logo_small.png'],
        }
    )

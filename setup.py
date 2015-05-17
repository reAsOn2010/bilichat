# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from bilichat import __version__

setup(
    name='bilichat',
    version=__version__,
    description='',
    long_description=open('README.rst').read(),
    url='git@github.com:reAsOn2010/bilichat.git',
    author='',
    author_email='',
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    zip_safe=False,
)

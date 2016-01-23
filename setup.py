#!/usr/bin/env python
"""Setup script for the project."""

from __future__ import print_function

import codecs
import os

from setuptools import find_packages, setup


def readme():
    """Try to read README.rst or return empty string if failed.

    :return: File contents.
    :rtype: str
    """
    abspath = os.path.realpath(os.path.join(os.path.dirname(__file__), 'README.rst'))
    file_handle = None
    try:
        file_handle = codecs.open(abspath, encoding='utf-8')
        return file_handle.read(131072)
    except IOError:
        return ''
    finally:
        getattr(file_handle, 'close', lambda: None)()


setup(
    author='@Robpol86',
    author_email='robpol86@gmail.com',
    classifiers=['Private :: Do Not Upload'],
    description='This is the template I use for my Python projects.',
    install_requires=[],
    keywords='replace me',
    license='MIT',
    long_description=readme(),
    name='replace_me',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/Robpol86/replace_me',
    version='0.0.1',
    zip_safe=True,
)

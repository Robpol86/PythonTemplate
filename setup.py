#!/usr/bin/env python
"""Setup script for the project."""

from __future__ import print_function

import codecs
import os

from setuptools import setup


def safe_read(path):
    """Try to read file or return empty string if failed.

    :param str path: Relative file path to read.

    :return: File contents.
    :rtype: str
    """
    abspath, file_handle = os.path.join(os.path.abspath(os.path.dirname(__file__)), path), None
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Text Processing :: Markup',
    ],
    description='This is the template I use for my Python projects.',
    install_requires=[],
    keywords='replace me',
    license='MIT',
    long_description=safe_read('README.rst'),
    name='replace_me',
    packages=['replace_me'],
    url='https://github.com/Robpol86/replace_me',
    version='0.0.1',
    zip_safe=True,
)

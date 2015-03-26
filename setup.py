#!/usr/bin/env python
"""Setup script for the project."""

import atexit
import codecs
import os
import re
import subprocess
import sys
from distutils.spawn import find_executable

import setuptools.command.sdist
from setuptools.command.test import test

_PACKAGES = lambda: [os.path.join(r, s) for r, d, _ in os.walk(NAME_FILE) for s in d if s != '__pycache__']
_VERSION_RE = re.compile(r"^__(version|author|license)__ = '([\w\.@]+)'$", re.MULTILINE)

CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Environment :: MacOS X',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Terminals',
    'Topic :: Text Processing :: Markup',
)
DESCRIPTION = 'This is the template I use for my Python projects.'
HERE = os.path.abspath(os.path.dirname(__file__))
KEYWORDS = 'replace me'
NAME = 'replace_me'
NAME_FILE = NAME
PACKAGE = False
VERSION_FILE = os.path.join(NAME_FILE, '__init__.py') if PACKAGE else '{0}.py'.format(NAME_FILE)


def _requires(path):
    """Read requirements file."""
    if not os.path.exists(os.path.join(HERE, path)):
        return list()
    file_handle = codecs.open(os.path.join(HERE, path), encoding='utf-8')
    requirements = [i for i in file_handle if i[0] != '-']
    file_handle.close()
    return requirements


def _safe_read(path, length):
    """Read file contents."""
    if not os.path.exists(os.path.join(HERE, path)):
        return ''
    file_handle = codecs.open(os.path.join(HERE, path), encoding='utf-8')
    contents = file_handle.read(length)
    file_handle.close()
    return contents


class PyTest(test):
    """Run tests with pytest."""

    description = 'Run all tests.'
    user_options = []
    CMD = 'test'
    TEST_ARGS = ['--cov-report', 'term-missing', '--cov', NAME_FILE, 'tests']

    def finalize_options(self):
        """Finalize options."""
        overflow_args = sys.argv[sys.argv.index(self.CMD) + 1:]
        test.finalize_options(self)
        setattr(self, 'test_args', self.TEST_ARGS + overflow_args)
        setattr(self, 'test_suite', True)

    def run_tests(self):
        """Run the tests."""
        # Import here, cause outside the eggs aren't loaded.
        pytest = __import__('pytest')
        err_no = pytest.main(self.test_args)
        sys.exit(err_no)


class PyTestPdb(PyTest):
    """Run tests with pytest and drop to debugger on test failure/errors."""

    _ipdb = 'ipdb' if sys.version_info[:2] > (2, 6) else 'pdb'
    description = 'Run all tests, drops to {0} upon unhandled exception.'.format(_ipdb)
    CMD = 'testpdb'
    TEST_ARGS = ['--{0}'.format(_ipdb), 'tests']


class PyTestCovWeb(PyTest):
    """Run the tests and open a web browser (OS X only) showing coverage information."""

    description = 'Generates HTML report on test coverage.'
    CMD = 'testcovweb'
    TEST_ARGS = ['--cov-report', 'html', '--cov', NAME_FILE, 'tests']

    def run_tests(self):
        """Run the tests and then open."""
        if find_executable('open'):
            atexit.register(lambda: subprocess.call(['open', os.path.join(HERE, 'htmlcov', 'index.html')]))
        PyTest.run_tests(self)


ALL_DATA = dict(
    author_email='robpol86@gmail.com',
    classifiers=CLASSIFIERS,
    cmdclass={PyTest.CMD: PyTest, PyTestPdb.CMD: PyTestPdb, PyTestCovWeb.CMD: PyTestCovWeb},
    description=DESCRIPTION,
    install_requires=_requires('requirements.txt'),
    keywords=KEYWORDS,
    long_description=_safe_read('README.rst', 15000),
    name=NAME,
    tests_require=_requires('requirements-test.txt'),
    url='https://github.com/Robpol86/{0}'.format(NAME),
    zip_safe=True,
)


# noinspection PyTypeChecker
ALL_DATA.update(dict(_VERSION_RE.findall(_safe_read(VERSION_FILE, 1500).replace('\r\n', '\n'))))
ALL_DATA.update(dict(py_modules=[NAME_FILE]) if not PACKAGE else dict(packages=[NAME_FILE] + _PACKAGES()))


if __name__ == '__main__':
    if not all((ALL_DATA['author'], ALL_DATA['license'], ALL_DATA['version'])):
        raise ValueError('Failed to obtain metadata from package/module.')
    setuptools.setup(**ALL_DATA)

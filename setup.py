#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools.command.test import test as TestCommand

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


README = open('README.rst').read()
HISTORY = open('HISTORY.rst').read().replace('.. :changelog:', '')

REQUIREMENTS = ['dbf', 'click', ]

TEST_REQUIREMENTS = ['pytest', ]


class PyTest(TestCommand):
    """ Mixin to integrate pytest with setup.py """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='dbfkit',
    version='0.2.0',
    description='DBF for humans',
    long_description=README + '\n\n' + HISTORY,
    author='Espartaco Palma',
    author_email='esparta@gmail.com',
    url='https://github.com/esparta/dbfkit',
    packages=[
        'dbfkit',
    ],
    package_dir={'dbfkit':
                 'dbfkit'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    cmdclass={'test': PyTest},
    license="Apache Software License",
    zip_safe=False,
    keywords='dbfkit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    test_suite='dbfkit.test_app',
    tests_require=TEST_REQUIREMENTS,
    entry_points='''
        [console_scripts]
        dbf2csv=dbfkit.cli:dbfread
    ''',
)

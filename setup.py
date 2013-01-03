#!/usr/bin/env python

from distutils.core import setup

setup(
    name='csvtools',
    version='1.0',
    description='Handy command line scripts for fussing with CSV files.',
    author='Will Ballard',
    author_email='wballard@mailfame.net',
    packages=['csvtools'],
    scripts=['scripts/csv_columns'],
)

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='csvtools',
    version='1.0',
    description='Handy command line scripts for fussing with CSV files.',
    author='Will Ballard',
    author_email='wballard@mailfame.net',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'csv_columns = csvtools.columns:main',
            'csv_cut = csvtools.cut:main',
        ]
    },
)

#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''Generate the cheraxrecords website'''

setup(
    name='cheraxrecords',
    version='0.1.0.0',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['cheraxrecords'],
    package_dir={'cheraxrecords': 'cheraxrecords'},
    entry_points={
        'console_scripts': ['cheraxrecords = cheraxrecords.main:main']
    },
    url='https://github.com/bjpop/cheraxrecords',
    license='LICENSE',
    description=('Generate the cheraxrecords website'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["jinja2>=2.10.1", "pyyaml"],
)

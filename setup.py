#!/usr/bin/env python3

from setuptools import setup

setup(
    name='pscanner',
    version='1.0',
    description='Watch stuff safely',
    url='https://github.com/envinyatar/pscanner',
    author='envinyatar',
    author_email='egidio.docile@gmail.com',
    license='GPL3',
    packages=['phscanner'],
    scripts=['bin/phs'],
    install_requires=['BeautifulSoup4']
)

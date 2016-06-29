#!/usr/bin/env python3

from setuptools import setup

setup(
    name='pscanner',
    version='1.0',
    description='Watch stuff safely',
    url='https://github.com/egdoc/phs',
    author='Egidio Docile',
    author_email='egidio.docile@gmail.com',
    license='GPL2',
    packages=['phscanner'],
    scripts=['bin/phs.py'],
    install_requires=['BeautifulSoup4']
)

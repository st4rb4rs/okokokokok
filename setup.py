# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='okokokokok',
    version='0.1.1',
    description='Simple choose your own story game',
    long_description=readme,
    author='Jack Adkins',
    author_email='barsofthestars.xyz@gmail.com',
    url='https://github.com/st4rb4rs/okokokokok',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


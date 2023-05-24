# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='perfectlurker',
    version='0.0.5',
    description='A twitchbot',
    long_description=readme,
    author='codingwithstrangers',
    author_email='root@codingwithstrangers.com',
    url='https://github.com/codingwithstrangers/perfect-lurker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

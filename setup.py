# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Ultrasonic Tardis',
    version='0.1.0',
    description='Doctor Who themed game that uses an Ultrasonic sensor connected to a Raspberry Pi in order to control a TARDIS and prevent it from crashing into the Daleks!',
    long_description=readme,
    author='Juan Pablo Yamamoto',
    author_email='me@jpyamamoto.com',
    url='https://github.com/JPYamamoto/handy_tardis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


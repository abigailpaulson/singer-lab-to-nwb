# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='singer_lab_to_nwb',
    version='0.1.0',
    description='NWB conversion scripts and tutorials.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steph Prince',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.yml']},
    install_requires=[
        'matplotlib', 'cycler', 'scipy', 'numpy', 'jupyter', 'h5py', 'pynwb',
        'nwbn-conversion-tools'],
)

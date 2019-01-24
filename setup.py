import glob
import os
import sys
from setuptools import find_packages, setup


additional_files = []
for filename in glob.iglob('./wooldridge/**', recursive=True):
    if '.csv.bz' in filename:
        additional_files.append(filename.replace('./wooldridge/', ''))

setup(
    name='wooldridge',
    version='0.1.0',
    author='Tetsu Haruyama',
    author_email='tetsu.yes@gmail.com',
    packages=find_packages(),
    # packages=['wooldridge'],
    package_dir={'wooldridge': './wooldridge'},
    include_package_data=True,
    package_data={'wooldridge': additional_files},
    url='https://github.com/spring-haru/wooldridge',
    license='LICENSE',
    description='Data sets for Introductory Econometrics: A Modern Approach (6th ed, J.M. Wooldridge)',
    long_description=open('README.md').read(),
    install_requires=[],
)

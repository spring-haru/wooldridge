import glob
from setuptools import find_packages, setup


additional_files = []
for filename in glob.iglob('./wooldridge/**', recursive=True):
    if '.csv.bz' in filename:
        additional_files.append(filename.replace('./wooldridge/', ''))

for filename in glob.iglob('./wooldridge/**', recursive=True):
    if '.txt' in filename:
        additional_files.append(filename.replace('./wooldridge/', ''))

setup(
    name='wooldridge',
    version='0.5.0',
    author='Tetsu Haruyama',
    author_email='tetsu.yes@gmail.com',
    packages=find_packages(),
    package_dir={'wooldridge': './wooldridge'},
    include_package_data=True,
    package_data={'wooldridge': additional_files},
    install_requires=['pandas'],
    url='https://github.com/spring-haru/wooldridge',
    license='LICENSE',
    description='Data sets from Introductory Econometrics: A Modern Approach (7th ed, J.M. Wooldridge)',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    keywords=['data', 'wooldridge', 'econometrics']
)

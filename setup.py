import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='Wooldridge',
     version='0.1',
     scripts=['wooldridge'] ,
     author="Tetsu Haruyama",
     author_email="tetsu.yes@gmail.com",
     description="Data sets for Introductory Econometrics: A Modern Approach (6th ed, J.M. Wooldridge)",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/spring-haru/wooldridge",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: GPLv3",
         "Operating System :: OS Independent",
     ],
 )

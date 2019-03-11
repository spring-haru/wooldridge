# Wooldridge Meets Python
### Data sets from _Introductory Econometrics: A Modern Approach_ (6th ed, J.M. Wooldridge)

## Description
A Python package which contains 111 data sets from one of the most famous **econometrics** textbooks for undergraduates.

## How to Use
First things first.
```
from wooldridge import *
```
To load a data set named `<dataset>`:
```
dataWoo('<dataset>')
```
It returns pandas `DataFrame`. Note that `<dataset>` is entered in strings. For example, to load a data set `mroz` into `df`:
```
df = dataWoo('mroz')
```
To show the description (e.g. variable definitions and sources) of a data set:
```
dataWoo('mroz', description=True)
```
To show the list of 111 data sets contained in the package
```
dataWoo()
```

## How to Install
```
pip install wooldridge
```
or
```
git clone https://github.com/spring-haru/wooldridge.git
pip install .
```

#### Reference
J.M. Wooldridge (2016) _Introductory Econometrics: A Modern Approach_, Cengage Learning, 6th edition.

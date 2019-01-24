# Wooldridge Meets Python
### Data sets for _Introductory Econometrics: A Modern Approach_ (6th ed, J.M. Wooldridge)

## Description
A Python package which contains 111 data sets from one of the most famous **econometrics** textbooks for undergraduates.

## How to Use
To import a `<dataset>`:
```
from wooldridge import <dataset>
```
For example, to load a data set `mroz` as pandas' `DataFrame` into `df`:
```
from wooldridge import mroz
df = mroz.load()
```
To show the description (e.g. variable definitions and sources) of a data set loaded, use one of the followings:
```
help(mroz.load)
?mroz.load
mroz.load?
```
To show the list of 111 data sets contained in the package when `<dataset>` is loaded:
```
<dataset>.wooldridge()
```
For example,
```
mroz.wooldridge()
```

## How to Install
```
git clone https://github.com/spring-haru/wooldridge.git
pip install .
```

## Notes on `401k` and `401ksubs`
Those two data sets are renamed with an **underscore** as follows:
* `401k` -> **`_401k`**
* `401ksubs` -> **`_401ksubs`**

import pandas as pd
import os
from os.path import abspath, join, split


lst = """\
  J.M. Wooldridge (2019) Introductory Econometrics: A Modern Approach,
  Cengage Learning, 7th edition.

  401k       401ksubs    admnrev       affairs     airfare
  alcohol    apple       approval      athlet1     athlet2
  attend     audit       barium        beauty      benefits
  beveridge  big9salary  bwght         bwght2      campus
  card       catholic    cement        census2000  ceosal1
  ceosal2    charity     consump       corn        countymurders
  cps78_85   cps91       crime1        crime2      crime3
  crime4     discrim     driving       earns       econmath
  elem94_95  engin       expendshares  ezanders    ezunem
  fair       fertil1     fertil2       fertil3     fish
  fringe     gpa1        gpa2          gpa3        happiness
  hprice1    hprice2     hprice3       hseinv      htv
  infmrt     injury      intdef        intqrt      inven
  jtrain     jtrain2     jtrain3       jtrain98    kielmc
  labsup     lawsch85    loanapp       lowbrth     mathpnl
  meap00_01  meap01      meap93        meapsingle  minwage
  mlb1       mroz        murder        nbasal      ncaa_rpi
  nyse       okun        openness      pension     phillips
  pntsprd    prminwge     prison        rdchem      rdtelec
  recid      rental      return        saving      school93_98
  sleep75    slp75_81    smoke         traffic1    traffic2
  twoyear    volat       vote1         vote2       voucher
  wage1      wage2       wagepan       wageprc     wine
"""


def _get_path(f):
    return split(abspath(f))[0]


def _find_full_file_path(path, dataset_to_open):
    """
    parameters:
        path: the folder of`py4macro.py`
        dataset_to_open: dataset to open

    return:
        a full file path of `dataset_to_open` including its file name"""

    for current_folder, sub_folders, _files in os.walk(path):
        if dataset_to_open in _files:
            return join(current_folder, dataset_to_open)


def data(name=None, description=False):

    if (name != None) & (description == False):

        full_file_path = _find_full_file_path(_get_path(__file__), name+".csv.bz2")
        return pd.read_csv(full_file_path, compression="bz2")

    elif (name != None) & (description == True):

        full_file_path = _find_full_file_path(_get_path(__file__), name+".txt")
        with open(full_file_path, 'r', encoding="utf-8") as f:
            print(f.read())

    elif name == None:
        print(lst)

def dataWoo(name=None, description=False):

    if (name != None) & (description == False):

        full_file_path = _find_full_file_path(_get_path(__file__), name+".csv.bz2")
        return pd.read_csv(full_file_path, compression="bz2")

    elif (name != None) & (description == True):

        full_file_path = _find_full_file_path(_get_path(__file__), name+".txt")
        with open(full_file_path, 'r', encoding="utf-8") as f:
            print(f.read())

    elif name == None:
        print(lst)

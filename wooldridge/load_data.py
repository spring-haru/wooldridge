from os.path import abspath, join, split
import pandas as pd


def get_path(f):
    return split(abspath(f))[0]


list = """\
  J.M. Wooldridge (2016) Introductory Econometrics: A Modern Approach,
  Cengage Learning, 6th edition.

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
  jtrain     jtrain2     jtrain3       kielmc      lawsch85
  loanapp    lowbrth     mathpnl       meap00_01   meap01
  meap93     meapsingle  minwage       mlb1        mroz
  murder     nbasal      nyse          okun        openness
  pension    phillips    pntsprd       prison      prminwge
  rdchem     rdtelec     recid         rental      return
  saving     sleep75     slp75_81      smoke       traffic1
  traffic2   twoyear     volat         vote1       vote2
  voucher    wage1       wage2         wagepan     wageprc
  wine"""


def dataWoo(name=None, description=False):
    if (name != None) & (description == False):
        return pd.read_csv(join(get_path(__file__), "datasets/" + name + ".csv.bz2"), compression="bz2")
    elif (name != None) & (description == True):
        with open(join(get_path(__file__), 'description/' + name + '.txt'), 'r', encoding="utf-8") as f:
            print(f.read())
    elif name == None:
        print(list)

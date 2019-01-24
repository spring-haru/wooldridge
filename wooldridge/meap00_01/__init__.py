def load():
    """name of dataset: meap00_01
    no of variables: 9
    no of observations: 1692

    +----------+-----------------------------------------------+
    | variable | label                                         |
    +----------+-----------------------------------------------+
    | dcode    | district code                                 |
    | bcode    | building code                                 |
    | math4    | % students satisfactory, 4th grade math       |
    | read4    | % students satisfactory, 4th grade reading    |
    | lunch    | % students eligible for free or reduced lunch |
    | enroll   | school enrollment                             |
    | exppp    | expenditures per pupil: expend/enroll         |
    | lenroll  | log(enroll)                                   |
    | lexppp   | log(exppp)                                    |
    +----------+-----------------------------------------------+

    Michigan Department of Education, www.michigan.gov/mde"""

    import wooldridge
    return wooldridge.load(__file__, "meap00_01.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)
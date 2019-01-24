def load():
    """name of dataset: meap01
    no of variables: 11
    no of observations: 1823

    +----------+-----------------------------------------------+
    | variable | label                                         |
    +----------+-----------------------------------------------+
    | dcode    | district code                                 |
    | bcode    | building code                                 |
    | math4    | % students satisfactory, 4th grade math       |
    | read4    | % students satisfactory, 4th grade reading    |
    | lunch    | % students eligible for free or reduced lunch |
    | enroll   | school enrollment                             |
    | expend   | total spending, $                             |
    | exppp    | expenditures per pupil: expend/enroll         |
    | lenroll  | log(enroll)                                   |
    | lexpend  | log(expend)                                   |
    | lexppp   | log(exppp)                                    |
    +----------+-----------------------------------------------+

    Michigan Department of Education, www.michigan.gov/mde"""

    import wooldridge
    return wooldridge.load(__file__, "meap01.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)
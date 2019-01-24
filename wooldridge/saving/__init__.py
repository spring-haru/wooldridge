def load():
    """name of dataset: saving
    no of variables: 7
    no of observations: 100

    +----------+-------------------------------+
    | variable | label                         |
    +----------+-------------------------------+
    | sav      | annual savings, $             |
    | inc      | annual income, $              |
    | size     | family size                   |
    | educ     | years educ, household head    |
    | age      | age of household head         |
    | black    | =1 if household head is black |
    | cons     | annual consumption, $         |
    +----------+-------------------------------+

    Unknown"""

    import wooldridge
    return wooldridge.load(__file__, "saving.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()
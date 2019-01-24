def load():
    """name of dataset: okun
    no of variables: 4
    no of observations: 47

    +----------+-------------------------------+
    | variable | label                         |
    +----------+-------------------------------+
    | year     | 1959 through 2005             |
    | pcrgdp   | percentage change in real GDP |
    | unem     | civilian unemployment rate    |
    | cunem    | unem - unem[_n-1]             |
    +----------+-------------------------------+

    Economic Report of the President, 2007, Tables B-4 and B-42."""

    import wooldridge
    return wooldridge.load(__file__, "okun.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)
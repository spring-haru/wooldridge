def load():
    """name of dataset: wine
    no of variables: 5
    no of observations: 21

    +----------+--------------------------------------+
    | variable | label                                |
    +----------+--------------------------------------+
    | country  |                                      |
    | alcohol  | liters alcohol from wine, per capita |
    | deaths   | deaths per 100,000                   |
    | heart    | heart disease dths per 100,000       |
    | liver    | liver disease dths per 100,000       |
    +----------+--------------------------------------+

    These data were reported in a New York Times article, December 28,
    1994."""

    import wooldridge
    return wooldridge.load(__file__, "wine.csv.bz2")


def wooldridge():
    import wooldridge
    print(wooldridge.dataset_list)
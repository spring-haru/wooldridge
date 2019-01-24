def load():
    """name of dataset: campus
    no of variables: 7
    no of observations: 97

    +----------+-----------------------+
    | variable | label                 |
    +----------+-----------------------+
    | enroll   | total enrollment      |
    | priv     | =1 if private college |
    | police   | employed officers     |
    | crime    | total campus crimes   |
    | lcrime   | log(crime)            |
    | lenroll  | log(enroll)           |
    | lpolice  | log(police)           |
    +----------+-----------------------+

    These data were collected by Daniel Martin, a former MSU
    undergraduate, for a final project. They come from the FBI Uniform
    Crime Reports and are for the year 1992."""

    import wooldridge
    return wooldridge.load(__file__, "campus.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()
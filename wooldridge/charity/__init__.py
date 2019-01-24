def load():
    """name of dataset: charity
    no of variables: 8
    no of observations: 4268

    +-----------+----------------------------------------+
    | variable  | label                                  |
    +-----------+----------------------------------------+
    | respond   | =1 if responded with gift              |
    | gift      | amount of gift, Dutch guilders         |
    | resplast  | =1 if responded to most recent mailing |
    | weekslast | number of weeks since last response    |
    | propresp  | response rate to mailings              |
    | mailsyear | number of mailings per year            |
    | giftlast  | amount of most recent gift             |
    | avggift   | average of past gifts                  |
    +-----------+----------------------------------------+

    P.H. Franses and R. Paap (2001), Quantitative Models in Marketing
    Research. Cambridge: Cambridge University Press. Professor Franses
    kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "charity.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()
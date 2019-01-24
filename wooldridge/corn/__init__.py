def load():
    """name of dataset: corn
    no of variables: 5
    no of observations: 37

    +----------+-------------------------+
    | variable | label                   |
    +----------+-------------------------+
    | county   | county number           |
    | cornhec  | corn per hectare        |
    | soyhec   | soybeans per hectare    |
    | cornpix  | corn pixels per hectare |
    | soypix   | soy pixels per hectare  |
    +----------+-------------------------+

    G.E. Battese, R.M. Harter, and W.A. Fuller (1988), “An Error-
    Components Model for Prediction of County Crop Areas Using Survey and
    Satellite Data,” Journal of the American Statistical Association 83,
    28-36. This small data set is reported in the article."""

    import wooldridge
    return wooldridge.load(__file__, "corn.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()
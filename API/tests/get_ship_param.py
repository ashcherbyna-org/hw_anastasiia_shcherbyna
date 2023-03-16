from API.structure.ship_param import Ship


def test_get_parameters(starships, parameters_ship):
    """
    :param parameters_ship: ship parameters
    :return: parameters
    """
    resp = starships.get()
    actual_res = Ship(
        resp.json()["manufacturer"],
        resp.json()['cost_in_credits'],
        resp.json()['length'],
        resp.json()["max_atmosphering_speed"],
    )
    del resp.json()["edited"]
    assert actual_res == parameters_ship



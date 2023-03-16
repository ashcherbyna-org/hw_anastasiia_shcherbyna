def test_get_resp(starships):
    """
    :param starships: name of ship
    :return: name
    """
    starship = starships.get()

    assert starship.json()["name"] == 'Death Star'


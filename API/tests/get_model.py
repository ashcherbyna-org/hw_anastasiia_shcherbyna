def test_get_model(starships):
    """
    :param starships: model parameter
    :return: name of model
    """
    model = starships.get()

    assert model.json()["model"] == 'DS-1 Orbital Battle Station'

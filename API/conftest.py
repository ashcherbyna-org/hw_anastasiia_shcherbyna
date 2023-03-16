import pytest

from API.structure.ship_param import Ship
from API.structure.starships import Starships


@pytest.fixture(scope="session")
def starships():
    yield Starships()


@pytest.fixture(scope="session")
def parameters_ship():
    yield Ship(manufacturer="Imperial Department of Military Research, Sienar Fleet Systems",
               cost_in_credits="1000000000000", length="120000", max_atmosphering_speed="n/a")

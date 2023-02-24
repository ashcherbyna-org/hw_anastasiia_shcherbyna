from HW17.human import Human
import pytest


@pytest.fixture(scope="session")
def human() -> Human:
    print("Preconditions")
    yield Human("Karl", 46, "male")
    print("Teardown")











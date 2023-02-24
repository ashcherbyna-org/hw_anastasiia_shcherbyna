from unittest import TestCase

from HW17.human import Human


def test_age(human):
    """

    :param human: Test human from fixture
    :return: test cover that Human age is correct
    """
    assert human.age == 46


def test_gender(human):
    """

    :param human: Test human from fixture
    :return: test cover that Human gender is correct
    """
    assert human.gender == "male"


def test_status(human):
    '''

    :param human: Test human from fixture
    :return: test cover that Human status is correct
    '''
    assert human.status == "alive"


def test_change_gender(human):
    '''

    :param human: Test human from fixture
    :return: new changer gander
    '''
    human.change_gender("female")
    assert human.gender == "female"


# Used None because I cannot apply self, and without None I cannot verify properly
def test_exception_change_gender(human):
    """
    :param human: Test human from fixture
    :return: Test invalid parameter
    """
    with TestCase.assertRaises(None, Exception):
        human.change_gender("male")


def test_exception_incorrect_gender(human):
    """

    :param human: Test human from fixture
    :return: Test invalid parameter
    """
    with TestCase.assertRaises(None, Exception):
        human.change_gender("trans")


def test_grow_limit(human):
    """

    :param human: Test human from fixture
    :return: Age and status
    """
    human.grow()
    assert human.age == 47
    assert human.status == "alive"


# Status was added in property, because I cannot verify scenario without that
def test_change_status():
    '''
    cannot use fixture because of that property was created
    :return: Dead status
    '''
    instance = Human("Tom", 100, "male")
    instance.grow()
    assert instance.age == 100
    assert instance.status == "dead"

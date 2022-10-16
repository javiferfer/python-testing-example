import pytest


@pytest.fixture(params=["a", "b", "c", "d", "e"])
def letter(request):
    yield request.param


def test_letter(letter):
    assert letter in {"a", "b", "c", "d", "e"}


@pytest.fixture(params=[1, 2, 3], ids=['foo', 'bar', 'baz'])
def mode(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param


def test_modes(mode):
    assert mode in [1, 2, 3]


@pytest.fixture(params=zip([1, 2, 3], ['foo', 'bar', 'baz']), ids=['foo', 'bar', 'baz'])
def mode_returning_ids(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param


def test_modes_returning_ids(mode_returning_ids):
    assert mode_returning_ids[0] in [1, 2, 3]
    assert mode_returning_ids[1] in ['foo', 'bar', 'baz']


# Tests all the combinations
def test_fixtureception(letter, mode):
    assert letter in {"a", "b", "c", "d", "e"}
    assert mode in [1, 2, 3]

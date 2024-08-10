import pytest


@pytest.fixture()
def f():
    print("bhargavi")
    x = 4
    y = 6
    return x + y


@pytest.fixture
def test_function(f):
    x = 10
    y = 20
    return x + y + f


def test_s(test_function, f):
    print(test_function+10 + f)
    print(test_function)
    assert test_function == 40

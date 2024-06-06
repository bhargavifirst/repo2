import pytest
@pytest.fixture()
def name():
    s = ("N.bbhargavi ", "chandana")
    return s
def test_a(name):
    l=len(name)
    print(l)
    print("my name is " + name[1])
@pytest.fixture()
def cal():
    num = (1, 2, 3, 4)
    return num
def test_add(cal):
    a = cal[1]+cal[3]
    print(a)

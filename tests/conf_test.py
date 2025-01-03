import pytest

@pytest.fixture()
def input_total():
    total=100
    return total


def test_div_5(input_total):
    assert input_total%5== 0

def test_div_2(input_total):
    assert input_total%2== 0

def test_div_19(input_total):
    assert input_total%19== 0

def test_div_10(input_total):
    assert input_total%10== 0
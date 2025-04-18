from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("5/0")


def test_value_error():
    with pytest.raises(ValueError):
        assert convert("cat/dog")

def test_value_error1():
    with pytest.raises(ValueError):
        assert convert("5/3")

def test_value_error2():
    with pytest.raises(ValueError):
        convert("6.5/3")

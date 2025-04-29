from seasons import main
import pytest

def test_main():
    assert  main("2024-04-29") == "Five hundred twenty-five thousand, six hundred  minutes"
    assert  main("2023-04-29") == "One million, fifty-two thousand, six hundred forty  minutes"


def test_value_error():
    with pytest.raises(ValueError):
        assert  main("2024-jan-31")

def test_value_error1():
    with pytest.raises(ValueError):
        assert  main("2023/12/28")
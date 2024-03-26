from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75.0
    assert convert("99/100") == 99.0
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ZeroDivisionError):
        convert("7/0")
def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

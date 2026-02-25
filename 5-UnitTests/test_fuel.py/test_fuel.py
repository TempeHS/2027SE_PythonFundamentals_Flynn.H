from fuel import get_percent
import pytest


def test_get_int():
    assert get_percent(5, 7) == 71
    with pytest.raises(ZeroDivisionError):
        get_percent(1, 0)
    with pytest.raises(ValueError):
        get_percent("cat", "dog")

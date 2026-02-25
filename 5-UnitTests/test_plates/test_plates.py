from plates import is_valid


def test_is_valid():
    assert is_valid("AAAAA") is True
    assert is_valid("AA22AA") is False
    assert is_valid("AA222") is True
    assert is_valid("AAAAAAA") is False
    assert is_valid("22AAAA") is False
    assert is_valid("AAAAAA") is True

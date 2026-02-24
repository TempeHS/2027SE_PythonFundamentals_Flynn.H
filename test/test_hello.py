from hello import hello


def test_hello():
    assert hello("david") == "hello, david"
    assert hello() == "hello, world"


def test_argument():
    assert hello("david") == "hello, david"

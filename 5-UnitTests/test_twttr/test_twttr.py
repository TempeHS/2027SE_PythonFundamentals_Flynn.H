from twttr import shorten_text


def test_shorten_test():
    assert shorten_text("flynn") == "flynn"
    assert shorten_text("xAEIOUaeioux") == "xx"
    assert shorten_text("HELLO") == "HLL"

from wordfind import find_word


def test_wordfind():
    assert find_word("story", "i") == 0
    assert find_word("story.txt", "i") == 2

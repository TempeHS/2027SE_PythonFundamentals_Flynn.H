from bank import money_owed


def test_money_owed():
    money = money_owed("hello")
    assert money == "$0"
    money = money_owed("hi")
    assert money == "$20"
    money = money_owed("greetings")
    assert money == "$100"

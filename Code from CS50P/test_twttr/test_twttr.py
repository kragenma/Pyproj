from twttr import shorten


def test_vowels():
    assert shorten("aeiou") == ""
def test_party():
    assert shorten("IT'S PARTY TIME!") == "T'S PRTY TM!"
def test_question():
    assert shorten("quandary") == "qndry"
def test_value():
    assert shorten("CS50")  == "CS50"
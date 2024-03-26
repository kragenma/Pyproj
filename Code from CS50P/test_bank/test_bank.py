from bank import value

try:
    def test_soclose():
        assert value("hi") == 20
    def test_missed():
        assert value("what's up") == 100
    def test_correct():
        assert value("hello") == 0
    def test_caps():
        assert value("HELLO") == 0
except:
    pass
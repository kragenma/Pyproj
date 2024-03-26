from plates import is_valid

def test_arrange():
    assert is_valid("CS50") == True
    assert is_valid("hey23") == True
    assert is_valid("w") == False
    assert is_valid("WW4WW") == False
    assert is_valid("wayyytooolong") == False
    assert is_valid("Ho.82") == False
    assert is_valid("nnw093") == False
    assert is_valid("99hi") == False
    assert is_valid("5342") == False
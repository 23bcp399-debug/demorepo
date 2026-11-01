from main import add, subtract

def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_add_negative():
    assert add(-2, 5) == 3

def test_subtract_negative():
    assert subtract(-2, 5) == -7
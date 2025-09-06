from app import add

def test_add():
    # These calls will log INFO messages
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, 20) == 30

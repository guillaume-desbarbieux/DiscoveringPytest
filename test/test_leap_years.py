from src.leap_years import is_leap

def test_divisible_by_400():
    assert is_leap(400) == True

def test_non_divisible_by_400():
    assert is_leap(405) == False

def test_divisible_by_100():
    assert is_leap(1800) == False

def test_divisible_by_4_not_100():
    assert is_leap(4) == True

def test_none_divisible_by_4():
    assert is_leap(5) == False
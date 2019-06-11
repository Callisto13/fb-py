import fizzbuzz

def test_that_number_is_divisible_by_three():
    assert fizzbuzz.is_divisible_by(3, 3) == True

def test_that_number_is_NOT_divisible_by_three():
    assert fizzbuzz.is_divisible_by(1, 3) == False

def test_that_number_is_divisible_by_five():
    assert fizzbuzz.is_divisible_by(5, 5) == True

def test_that_number_is_NOT_divisible_by_five():
    assert fizzbuzz.is_divisible_by(1, 5) == False

def test_that_number_is_divisible_by_three_and_five():
    assert fizzbuzz.is_divisible_by(15, 15) == True

def test_that_number_is_NOT_divisible_by_three_and_five():
    assert fizzbuzz.is_divisible_by(1, 15) == False

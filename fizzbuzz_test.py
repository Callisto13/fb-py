import fizzbuzz

def test_that_number_is_divisible_by_three():
    assert fizzbuzz.is_divisible_by_three(3) == True

def test_that_number_is_NOT_divisible_by_three():
    assert fizzbuzz.is_divisible_by_three(1) == False

def test_that_number_is_divisible_by_five():
    assert fizzbuzz.is_divisible_by_five(5) == True

def test_that_number_is_NOT_divisible_by_five():
    assert fizzbuzz.is_divisible_by_five(1) == False

def test_that_number_is_divisible_by_three_and_five():
    assert fizzbuzz.is_divisible_by_three_and_five(15) == True

def test_that_number_is_NOT_divisible_by_three_and_five():
    assert fizzbuzz.is_divisible_by_three_and_five(1) == False

def is_divisible_by(number, divisor):
     return number % divisor == 0

def says(number):
    if is_divisible_by(number, 15):
        return "fizzbuzz"
    elif is_divisible_by(number, 3):
        return "fizz"
    elif is_divisible_by(number, 5):
        return "buzz"
    else:
        return number

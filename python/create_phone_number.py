"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    new_n = "".join(map(str,n))
    return "(" + new_n[:3] + ") " + new_n[3:6] + "-" + new_n[6:]



def basic_test_cases():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"

    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"

    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"

basic_test_cases()
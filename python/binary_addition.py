"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""
def DecimalToBinary(num):
    if num >= 1:
        print(num)
        DecimalToBinary(num // 2)
        print(num % 2)

def add_binary(a,b):
    num = a + b
    if num == 1:
        return "1"
    elif num == 0:
        return "0"
    binary_string = ""
    while num >= 1:
        num = num//2
        binary_string+= str(num%2)
    print(binary_string)
    return binary_string

def test()-> None:
    assert add_binary(1,1) == "10"
    assert add_binary(0,1) == "1"
    assert add_binary(1,0) == "1"
    assert add_binary(2,2) == "100"
    assert add_binary(51,12) == "111111"

# test()
DecimalToBinary(4)
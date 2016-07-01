# Implement a function that successfully adds two numbers together and returns their solution in binary. The conversion can be done before, or after the addition of the two.
#
# The binary number returned should be a string!
#
# Test.assert_equals(add_binary(1,1),"10")
# Test.assert_equals(add_binary(0,1),"1")
# Test.assert_equals(add_binary(1,0),"1")
# Test.assert_equals(add_binary(2,2),"100")
# Test.assert_equals(add_binary(51,12),"111111")

def find_highest_power_2(num):
    n=0
    while 2**n <= num:
        n += 1
    return n-1

def add_binary(a,b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)


def add_binary_(a,b):
    return bin(a+b)[2:]
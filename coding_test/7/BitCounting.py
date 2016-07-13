# print(bin(1234))  # 0b10011010010
# # 10011010010
#
# print(bin(10)) # 0b1010
# print(bin(9)) # 0b1001
# print(bin(8)) # 0b1000
# print(type(bin(5))) # <class 'str'>
#
# print(int('0110', 2)) # 6
# print(int('1000', 2)) # 8
# print(int('1111', 2)) # 15
# print(int('0111', 2)) # 7

# Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
  strBin = bin(n)
  return strBin.count('1')

print(countBits(8))
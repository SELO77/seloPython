# Your objective is to complete a recursive function reverse() that receives str as String and returns the same string in reverse order
#
# Rules:
#
# reverse function should be executed only N times. N = length of the input string
# helper functions are not allowed
# changing the signature of the function is not allowed
# Examples:
#
# reverse("hello world") = "dlrow olleh" (N = 11)
# reverse("abcd") = "dcba" (N = 4)
# reverse("12345") = "54321" (N = 5)

# def reverse(str):
#   result = ""
#   count = 0
#   for i in str:
#     if(count < len(str)):
#       result += (str[len(str) - count - 1])
#       count += 1
#
#   return result
#
# print(reverse("hello"))
def recursiveReverse(arg):
  if len(arg) == 0: return ""
  return arg[-1] + recursiveReverse(arg[0:-1])

print(recursiveReverse("1"))

list2 = ["h","e","l"]
# f = "".join(list2)
# print(f)
# print(list2.pop(-2))

# def fib(n):
#   print(n)
#   if n == 0:
#       return 0
#   elif n == 1:
#       return 1
#   else:
#       return fib(n-1) + fib(n-2)
#
# print(fib(10))
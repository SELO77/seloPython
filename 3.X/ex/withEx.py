from _io import TextIOWrapper
import trace

class JustDoItClass():

  def __init__(self):
    print("init")

  def __enter__(self):
    print("enter")

  def __exit__(self, exc_type, exc_val, exc_tb):
    print("exit")

  def __str__(self):
    print("str")

  def myFNC(self):
    print('Hello'[0])



justDoItClass = JustDoItClass()

theFile = open('./file/testFile')
print(str(type(theFile)))

#TextIOWrapper.__exit__()

with theFile as inFile:
  for line in inFile:
    print(line)



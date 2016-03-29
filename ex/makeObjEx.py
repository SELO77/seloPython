# from http import client
#
# client.HTTPConnection()
import asyncio
import traceback

#객체 레퍼런스 테스트
class HumanClass():
  name = ""
  sex = ""

  def __init__(self):
    pass


def testFNC():
  for i in range(2):
    person = HumanClass()
    print(person)

testFNC()
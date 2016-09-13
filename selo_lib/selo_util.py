# -*- coding: utf-8 -*-
# 회사 코드 컨벤션을 준수한 코드

# import asyncio
# import socket
# import traceback
# from decimal import *
# from datetime import datetime, timedelta
# from geopy.distance import vincenty


# FIXME: color_console version 0.1
def cc(content="", type=None):

  if content is None:
    return

  content = str(content)
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  END = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

  if type == "header": # 보라색
    print(HEADER + content + END)

  elif type == "okblue":
    print(OKBLUE + content + END)

  elif type == "okgreen":
    print(OKGREEN + content + END)

  elif type == "warning":
    print(WARNING + content + END)

  elif type == "fail":
    print(FAIL + content + END)

  elif type == "bold":
    print(BOLD + content + END)

  elif type == "underline":
    print(UNDERLINE + content + END)

  elif type is None:
    print(content)


# def decimal_round(num, unit=0):
#   result = None
#   unit = str(unit)
#   if isinstance(num, Decimal):
#     result = num.quantize(Decimal(unit), rounding=ROUND_UP)
#   else:
#     result = Decimal(num).quantize(Decimal(unit), rounding=ROUND_UP)
#   return result


# # 서버시간을 입력받아 GMT+9(한국 현지시간 계산)
# def get_GMT(hours):
#   if isinstance(hours, int):
#     return datetime.utcnow() + timedelta(hours=hours)
#   else:
#     raise Exception('get_GMT parameters must be int. you have given type of %s'
#                     %type(hours))

# # [[위도, 경도], [위도, 경도]] 형식을 받아 두 지점사이의 거리 계산결과를 리턴하는 함수
# def cal_distance(list):

#   temp_list = list
#   for i, v in enumerate(list):
#     temp_list[i] = tuple(v)
#   return vincenty(temp_list[0], temp_list[1]).kilometers

# # unicode를 byte string으로 변환
# def to_bytes(bytes_or_str):
#   if isinstance(bytes_or_str, str):
#     value = bytes_or_str.encode('utf-8')
#   else:
#     value = bytes_or_str
#   return value

# # String 타입의 true, false를 전달 받아 boolean 타입으로 변경
# def to_TrueFalse(str_truefalse):
#   if isinstance(str_truefalse, str):
#     if str_truefalse.lower() == "true":
#       return True
#     elif str_truefalse.lower() == "false":
#       return False


# @asyncio.coroutine
# def write_file(path, *args):
#   # first argument must be path

#   if not isinstance(path, str):
#     raise Exception("path must be str")

#   if not args:
#     raise Exception("need arguments")

#   try:
#     cc("== write_file ==", 'okgreen')
#     with open(path, 'a') as f:
#       for v in args:
#         f.write(":%s"%str(v))
#       f.close()
#   except:
#     print(traceback.format_exc())

# # FIXME: deprecated color_console version 0.0 위 0.1 버전을 사용하세요.
# def color_console(type=None, content=""):

#   if content is None:
#     return

#   # 운영 반영
#   if content:
#     return

  # content = str(content)
  # HEADER = '\033[95m'
  # OKBLUE = '\033[94m'
  # OKGREEN = '\033[92m'
  # WARNING = '\033[93m'
  # FAIL = '\033[91m'
  # END = '\033[0m'
  # BOLD = '\033[1m'
  # UNDERLINE = '\033[4m'
  #
  # if type == "header": # 보라색
  #   print(HEADER + content + END)
  #
  # elif type == "okblue":
  #   print(OKBLUE + content + END)
  #
  # elif type == "okgreen":
  #   print(OKGREEN + content + END)
  #
  # elif type == "warning":
  #   print(WARNING + content + END)
  #
  # elif type == "fail":
  #   print(FAIL + content + END)
  #
  # elif type == "bold":
  #   print(BOLD + content + END)
  #
  # elif type == "underline":
  #   print(UNDERLINE + content + END)
  #
  # elif type is None:
  #   print(content)


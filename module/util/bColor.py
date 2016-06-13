from inspect import currentframe, getframeinfo

def color_console(type=None, content=""):

  if content is None:
    return

  # cf = currentframe()
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
import traceback

def wirte_file(path, *args):
  # first argument must be path
  if not isinstance(path, str):
    raise Exception("path must be str")
  if not args:
    raise Exception("need arguments")
  try:
    with open(path, 'a') as f:
      for v in args:
        f.write(":%s"%str(v))
  except:
    print(traceback.format_exc())

wirte_file('./resources/log1',
           "12312312",
           'hello', ['asdkasld', 123123])
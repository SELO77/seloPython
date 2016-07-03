

def test(first, *hi, **args):
  print(first)
  print(hi)
  print(args['email'])


test("sdf", 1234, email="sad@naver.com")
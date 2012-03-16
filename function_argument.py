# this is function test1
#
#
def test1(*args):
  if args:
    for item in args:
      print item

def foo(func, args):
  return func(*args)

def test():
  foo(test1,[1,2,3,4])
  foo(test1,["this is a test", 3])

if __name__ == '__main__':
  test()


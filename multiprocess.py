from multiprocessing import Process, Lock, Pool
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def info(title):
    print title
    print 'module name:', __name__
    #print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

def f1(lock, num):
  lock.acquire()
  print "hello world %d, %d" % (os.getpid(), num)
  lock.release()

def f2(x):
  print os.getpid(), x
  return x*x

def test1():
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

# test the synchronization between processes
def test2():
  lock = Lock()
  for num in range(10):
    Process(target=f1, args=(lock, num)).start()

# test a pool of process
def test3():
  processPool = Pool(processes=4)
  result = processPool.apply_async(f2,[10])
  print result.get(timeout=1)
  print processPool.map(f2, range(10))
  processPool.close()
  processPool.join()

def main():
  print sys.path
  #test1()
  #test2()
  test3()

if __name__ == '__main__':
  main()

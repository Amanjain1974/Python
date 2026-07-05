import sys
sys.setrecursionlimit(2000)
n=0
def python():
    global n
    n = n + 1
    print('python', n)

    python()
import sys

if __name__ == "__main__":
    N, M = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    l = []
    for i in range(N):
        a, b = sys.stdin.readline().strip().split(' ')
        l.append((a,b))
    print l
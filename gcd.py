import sys
from fractions import gcd

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    numbers = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    Q = int(sys.stdin.readline().strip())
    l = []
    for i in range(Q):
        g = int(sys.stdin.readline().strip())
        l.append(g)
    for g in l:
        count = 0
        if g in numbers:
            count += 1
        for a in numbers:
            for b in numbers:
                if a != b and b > a:
                    da_gcd = gcd(a, b)
                    if da_gcd == g:
                        count += 1
        print count
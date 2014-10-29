import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    l = []
    for i in range(n):
        a, b = sys.stdin.readline().strip().split(' ')
        a, b = int(a), int(b)
        l.append((a, b))
    for (a,b) in l:
        if a % 5 == 0 and b % 5 == 0:
            print "TRUE"
        elif a % 13 == 0 and b % 13 == 0:
            print "TRUE"
        elif a % 17 == 0 and b % 17 == 0:
            print "TRUE"
        elif a % 29 == 0 and b % 29 == 0:
            print "TRUE"
        elif a % 37 == 0 and b % 37 == 0:
            print "TRUE"
        else:
            print "FALSE"
import sys

if __name__ == "__main__":
    S, E, P, N = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    user_picks = []
    lottery_set = []
    for i in range(N):
        user_picks.append(int(sys.stdin.readline().strip()))
    for pick in user_picks:
        for i in range(S, E+1):
            if str(pick) in str(i):
                lottery_set.append(i)
    lottery_set = sorted(lottery_set)
    if P > len(lottery_set) or P < 1:
        print "DOES NOT EXIST"
    else:
        print lottery_set[P-1]
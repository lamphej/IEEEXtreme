import sys

if __name__ == "__main__":
    max_len = 0
    user_input = list(sys.stdin.readline().strip())
    results = []
    outstr = ''
    if ''.join(reversed(user_input)) == user_input:
        max_len = len(user_input)
    else:
        for i in range(len(user_input)):
            if user_input.count(user_input[i]) >= 2:
                outstr += user_input[i]
    print max_len
    print outstr
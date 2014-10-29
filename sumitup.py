import sys


def cyclic_thing(state, operation):
    o = state[:]
    for i in range(len(state)):
        i_operation = i + operation
        if i_operation >= len(state):
            o[i_operation - len(state)] = o[i_operation - len(state)] + state[i]
        else:
            o[i_operation] = o[i_operation] + state[i]
    return o


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    numbers = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    Q = int(sys.stdin.readline().strip())
    cyclic = numbers
    for i in range(Q):
        op = int(sys.stdin.readline().strip())
        cyclic = cyclic_thing(cyclic, op)
    total = sum(cyclic) % (pow(10, 9) + 7)
    print total
__author__ = 'Jim'
import sys


def get_next_cell(seq):
    """
    Gets the next cell state
    """
    a = seq[0]
    b = seq[1]
    c = seq[2]
    if a == 1 and b == 1 and c == 1:
        return 0
    elif a == 1 and b == 1 and c == 0:
        return 0
    elif a == 1 and b == 0 and c == 1:
        return 0
    elif a == 1 and b == 0 and c == 0:
        return 1
    elif a == 0 and b == 1 and c == 1:
        return 1
    elif a == 0 and b == 1 and c == 0:
        return 1
    elif a == 0 and b == 0 and c == 1:
        return 1
    elif a == 0 and b == 0 and c == 0:
        return 0

def get_chr(v):
    return "*" if v else ' '

def print_state(state):
    global state_index, keep_going
    if keep_going:
        print "{:<3}".format(str(state_index)) + " -%s-" % ''.join([get_chr(v) for v in state])
    state_index += 1

def get_next_state(state):
    global keep_going
    next_state = [0 for i in range(len(state))]
    next_state[0] = get_next_cell([0, state[0], state[1]])
    for i in range(0, len(state)-2):
        next_state[i+1] = get_next_cell([state[i], state[i+1], state[i+2]])
    next_state[-1] = get_next_cell([state[-2], state[-1], 0])
    keep_going = state != next_state
    return next_state

if __name__ == "__main__":
    rule, iterations, n, rep = sys.stdin.readline().strip().split(' ')
    # print "Rule #: %s\nIterations: %s\nN: %s\nInput: %s" % (rule, iterations, n, rep)
    binary_format = '{0:0%sb}' % n
    current_state = [int(a) for a in list(binary_format.format(int(rep)))]
    # print "Initial State: %s" % current_state
    state_index = 1
    keep_going = True
    print_state(current_state)

    for i in range(int(iterations)-1):
        if keep_going:
            next_state = get_next_state(current_state)
            print_state(next_state)
            current_state = next_state
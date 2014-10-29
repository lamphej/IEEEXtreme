import sys

if __name__ == "__main__":
    sequence = [int(a) for a in sys.stdin.readline().split(' ')]
    iterations = sequence[0]
    sequence = sequence[1::]
    index = 0
    output = ""
    l = []
    l.append(sequence)
    max_length = len(sequence)
    lastlen = 0
    for i in range(iterations):
        #print "Sequence: %s" % sequence
        while index < len(sequence):
            c_int = sequence[index]
            count = 1
            i2 = index + 1
            while i2 < len(sequence) and (sequence[i2] == sequence[index]):
                count += 1
                i2 += 1
            index = i2
            output += str(count) + ' ' + str(c_int) + ' '
            #print "%s %s's" % (count, c_int)
            count = 0
        index = 0
        i2 = 0
        output = output.strip()
        jones = [int(a) for a in output.split(' ')]
        l.append(jones)
        if len(jones) > max_length:
            max_length = len(jones)
        output = ""
        sequence = jones
        jones = []
    for thing in l:
        if len(thing) < max_length:
            newlen = 2 * max_length - 1
            difference = newlen  - (2*len(thing)-1)
            afterdots = difference / 2
            beforedots = afterdots + (difference % 2)
            new_output = ''.join(['.' * beforedots]) + ' '.join([str(t) for t in thing]) + ''.join(['.' * afterdots])
            if len(new_output )>newlen:
                new_output=new_output[:-1:]
            print new_output
            lastlen = len(thing)
        else:
            print ' '.join([str(t) for t in thing])
            lastlen = len(thing)
    print lastlen
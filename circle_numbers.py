import sys

if __name__ == "__main__":
    tmp = sys.stdin.readline()
    n, m, k = [int(t) for t in tmp.strip().split(' ')]
    numbers = [n for n in sys.stdin.readline().strip().split(' ')]
    the_smallest = 2147483647
    all_smallest = []
    for i in range(len(numbers)):
        if i + m > len(numbers):
            seq = numbers[i::]
            start = numbers[0:m-len(seq)]
            for s in start:
                seq.append(s)
        else:
            seq = numbers[i:i+m]
        seq = [int(a) for a in seq]
        sorted_seq = sorted(seq)
        kth_smallest = sorted_seq[k-1]
        if kth_smallest < the_smallest:
            the_smallest = kth_smallest
    print the_smallest
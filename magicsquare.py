import sys

if __name__ == "__main__":
    size = int(sys.stdin.readline().strip())
    matrix = []
    for i in range(size):
        matrix.append([int(a) for a in sys.stdin.readline().strip().split(' ')])
    x, y = 0, 0
    diag_sum = 0
    anti_sum = 0
    while x < len(matrix[0]) and y < len(matrix):
        diag_sum += matrix[y][x]
        x += 1
        y += 1
    x = len(matrix[0]) - 1
    y = 0
    while x >= 0 and y < len(matrix):
        anti_sum += matrix[y][x]
        x -= 1
        y += 1
    bad_rows = []
    for row in matrix:
        s = sum(row)
        if s != diag_sum:
            bad_rows.append((matrix.index(row)+1))
    for x in range(len(matrix[0])):
        x_sum = 0
        for y in range(len(matrix)):
            x_sum += matrix[y][x]
        if x_sum != diag_sum:
            bad_rows.append(0 - (x+1))
    if diag_sum != anti_sum:
        bad_rows.append(0)
    bad_rows = sorted(bad_rows)
    print len(bad_rows)
    for b in bad_rows:
        print b
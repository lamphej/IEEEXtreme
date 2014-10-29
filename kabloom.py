import sys

if __name__ == "__main__":
    card_count = int(sys.stdin.readline().strip())
    while card_count != 0:
        card_row_1 = sys.stdin.readline().strip().split(' ')
        card_row_2 = sys.stdin.readline().strip().split(' ')
        card_count = int(sys.stdin.readline().strip())
        for a in card_row_1:
            if not a in card_row_2:
                card_row_1[card_row_1.index(a)] = '*'
        for b in card_row_2:
            if not b in card_row_1:
                card_row_2[card_row_2.index(b)] = '*'
        print ' '.join(card_row_1)
        print ' '.join(card_row_2)
import sys

if __name__ == "__main__":
    num_robbers, load_capacity = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    line = sys.stdin.readline().strip()
    loot = []
    while line != "END":
        loot_name, loot_amount, loot_value = line.split(',')
        loot_amount = float(loot_amount)
        loot_value = float(loot_value)
        loot.append((loot_name, loot_amount, loot_value, loot_value/loot_amount))
        line = sys.stdin.readline().strip()
    loot = sorted(loot, key=lambda x: x[0])
    best_loot = sorted(loot, key=lambda x: x[3], reverse=True)
    print best_loot
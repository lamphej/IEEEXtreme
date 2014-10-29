import sys, math

if __name__ == "__main__":
    n, m = [int(a) for a in sys.stdin.readline().strip().split(' ')]
    heroes = []
    for i in range(n):
        hero_name, hero_type, hero_wl = sys.stdin.readline().strip().split(',')
        hero_wl = [float(a) for a in hero_wl.split(':')]
        hero_wl = math.floor((hero_wl[0] / (hero_wl[0] + hero_wl[1]))*100)
        hero_zi = float(1.0 / (float(i) + 1.0))
        hero_quality = hero_wl / hero_zi
        heroes.append((hero_name, hero_type, hero_quality, i+1))
    heroes = sorted(heroes, key=lambda x: x[2], reverse=True)[:m:]
    for hero in heroes:
        print hero[0]
    print " "
    print "This set of heroes: "
    set_intelligence = [hero for hero in heroes if hero[1] == 'Intelligence']
    set_strength = [hero for hero in heroes if hero[1] == 'Strength']
    set_agility = [hero for hero in heroes if hero[1] == 'Agility']
    set_intelligence = float(len(set_intelligence)) / float(len(heroes)) * 100
    set_strength = float(len(set_strength)) / float(len(heroes)) * 100
    set_agility = float(len(set_agility)) / float(len(heroes)) * 100
    print "Contains %.2f percentage of Intelligence" % set_intelligence
    print "Contains %.2f percentage of Strength" % set_strength
    print "Contains %.2f percentage of Agility" % set_agility
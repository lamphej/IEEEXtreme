import sys

if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())
    for i in range(m):
        n, f, t, l = [int(a) for a in sys.stdin.readline().strip().split(' ')]
        stations = {}
        for j in range(n):
            distance, price = [int(a) for a in sys.stdin.readline().strip().split(' ')]
            stations[distance] = price
        sorted_stations = sorted(stations.items(), key=lambda x: x[0])
        print sorted_stations
        cheapest_station = sorted(stations.items(), key=lambda x: x[1])[0]
        print cheapest_station
        gas_to_cheapest = cheapest_station[0] - t
        print "Need %s litres" % gas_to_cheapest
        nearer_station = sorted_stations[sorted_stations.index(cheapest_station)-1]
        print "SHould go to %s" % nearer_station
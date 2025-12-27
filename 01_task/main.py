from random import shuffle
import heapq


def prepare_cables(size: int) -> [int]:
    cables = []

    for i in range(size):
        cables.append((i+1) * 5)
    # to make it randomly distributes in the list
    shuffle(cables)

    return cables


def connect_cable(cables: [int]) -> int:
    # Firstly we have to connect the shortest cables to keep the total cost lower
    # Use heap to track the shortest cable
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:  # in the end we should have single cable
        shortest_cable_1 = heapq.heappop(cables)
        shortest_cable_2 = heapq.heappop(cables)
        print(f"Pop cables {shortest_cable_1}, {shortest_cable_2}")

        new_cable = shortest_cable_1 + shortest_cable_2
        total_cost += new_cable
        # return a new cable to the heap, the size of heap reduces by 1
        heapq.heappush(cables, new_cable)

    return total_cost


def main():
    cables = prepare_cables(5)
    total_cost = connect_cable(cables)
    print(f"Total cost is {total_cost}")


if __name__ == '__main__':
    main()

import heapq


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    h = []

    for items in lists:
        for item in items:
            heapq.heappush(h, item)

    return [heapq.heappop(h) for _ in range(len(h))]


def merge_k_lists_v2(lists: list[list[int]]) -> list[int]:
    return list(heapq.merge(*lists))


def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
    print("Відсортований список v2:", merge_k_lists_v2(lists))


if __name__ == '__main__':
    main()

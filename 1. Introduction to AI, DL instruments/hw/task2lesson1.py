items = [1, 5, 6, 9, 8, 7, 2, 3, 4]
shuffled_items = [2, 3, 4, 1, 6, 5, 7, 9, 8]
items.sort(key=lambda x: shuffled_items.index(x))

print(items)

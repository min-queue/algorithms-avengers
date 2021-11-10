from collections import Counter


a = [1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 0, 0]

b = Counter(a)

print(b)
print(b.most_common(4))

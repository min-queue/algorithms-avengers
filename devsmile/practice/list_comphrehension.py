import re

# lambda expression
print(list(map(lambda x: x + 10, [1, 2, 3])))

# list comphrehension
print([n * 2 for n in range(1, 11) if n % 2 == 1])

# list comphrehension
str1 = "This Is It! Dev-SmIle"
str1s = [
    str1[i : i + 2].lower()
    for i in range(len(str1) - 1)
    if re.findall("[a-z]{2}", str1[i : i + 2].lower())
]

print(str1s)

a = {"a", "b", "c"}
print(type(a))

a = {"a": "A", "b": "B", "c": "C"}
print(type(a))

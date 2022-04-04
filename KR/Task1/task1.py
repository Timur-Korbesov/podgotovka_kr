import sys

text = sys.stdin.readlines()
char = text[-1].rstrip()
text.remove(text[-1])

index = 10000
res = ""

for string in text:
    string = string.strip()[::-1]
    if char in string and string.index(char) < index:
        index = string.index(char)
        res = string

res = res[::-1]

lst = []

count = 0

for el in res:
    if el != char:
        count += 1
    else:
        count += 1
        if count != 0:
            lst.append(count)
        count = 0
print(max(lst))
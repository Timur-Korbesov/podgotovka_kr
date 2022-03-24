import json

f = open("task2_file.json", "r")
sl = json.load(f)

temp = []
for s in sl:
    if s["hide"] > 10:
        temp.append(tuple(s.values()))
temp.sort(key=lambda x: x[0], reverse=True)
print(temp)
f.close()

f = open("hide_and_seek.csv", "w")
print("name,size,hide,magic", file=f)

for element in temp:
    print(*element, file=f, sep=',')
print(sl[0].keys())
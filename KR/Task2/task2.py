import json

filename = input()

file = open(filename, "r")
text = file.readlines()
results = {}

for line in text[1:]:
    line = line.rstrip().split(":")
    if line[1] in results.keys():
        results[line[1]].append(line[2])
        results[line[1]] = sorted(results[line[1]])
    else:
        results[line[1]] = []
        results[line[1]].append(line[2])

f = open("events.json", "w")
f.write(json.dumps(results))
f.close()
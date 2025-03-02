import csv
import json
import collections

m = collections.defaultdict(list)

with open('output.csv', 'r', encoding='utf-8') as file:
    line = file.readlines()
    for el in line:
        data = el.split(',')
        m["locations"].append([float(data[0]), float(data[1][:-2])])

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(m, file, indent=4)
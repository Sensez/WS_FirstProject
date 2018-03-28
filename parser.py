import csv

import pandas as pd

csv_file = pd.read_csv('vgsalesTop20.csv')
csv_file.drop_duplicates(inplace=True, keep='first')
relations = []
triples = []
counter = 1

for row in csv_file:
    relations.append(row)
for header in relations:
    if header != 'Rank':
        for value in csv_file[header]:
            triples.append((counter, header, value))
            counter += 1
    counter = 1

f = open('clean_sales.csv', "w", encoding='utf-8')
writer = csv.writer(f)
for sub, pred, obj in triples:
    writer.writerow([sub, pred, obj])
f.close()

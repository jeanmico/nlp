import os
import json
from bs4 import BeautifulSoup

fpath = os.path.join(os.path.sep, 'Users', 'student', 'nlp', 'clinical_classify')
fname = '__data_export.json'
ref_name = 'ref_clinical_items.txt'
out_name = 'filtered_data.txt'

fields = []
with open(os.path.join(fpath, ref_name), 'r') as f:
    for line in f:
        tmp = line.strip().split(',')
        if tmp[1].strip() == 'y':
            fields.append(tmp[0])
print(len(fields))

with open(os.path.join(fpath, fname), 'r') as f:
    data = json.load(f)

filtered_data = []
for study, val in data.items():
    tmp = [study]
    for item in fields:
        if item in val:
            try:
                tmp.append(BeautifulSoup(val[item], 'lxml').get_text().replace('\n', ' '))
            except:
                tmp.append(val[item])
        else:
            tmp.append('-')
    filtered_data.append(tmp)

with open(os.path.join(fpath, out_name), 'w+') as out:
    out.write('\n'.join(' | '.join(str(x) for x in trial) for trial in filtered_data))

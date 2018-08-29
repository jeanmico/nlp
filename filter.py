import os
import json
from bs4 import BeautifulSoup

def html_strip(text):
    try:
        return BeautifulSoup(text, 'lxml').get_text().replace('\n', ' ')
    except:
        return text


def read_fields(path, name):
    fields = []
    with open(os.path.join(path, name), 'r') as f:
        for line in f:
            tmp = line.strip().split(',')
            if tmp[1] == 'y':
                fields.append((tmp[0], tmp[2]))
    return fields


def add_item_type(field_name, field_type, field_val):
    # the field type is passed in case some should be handled differently
    # it is not currently used
    if field_type == 'n':
        return html_strip(field_val)


def add_items(fields, data):
    filtered = []
    unused = set()
    for study, val in data.items():
        tmp = [study]
        for item in fields:
            if item[0] in val:
                tmp.append(add_item_type(item[0], item[1], val[item[0]]))
            else:
                tmp.append('-')
                unused.add(item[0])
        filtered.append(tmp)
    print(unused)
    return filtered

fpath = os.path.join(os.path.sep, 'Users', 'student', 'nlp', 'clinical_classify')
fname = '__data_export.json'
ref_name = 'ref_clinical_items.txt'
out_name = 'filtered_data.txt'
head_name = 'headers.txt'

fields = read_fields(fpath, ref_name)
print(fields)

with open(os.path.join(fpath, fname), 'r') as f:
    data = json.load(f)

filtered_data = add_items(fields, data)

# write the filtered data to a file
with open(os.path.join(fpath, out_name), 'w+') as out:
    out.write('\n'.join('~~'.join(str(x) for x in trial) for trial in filtered_data))

# write the headers to a file
headers = list(fields[i][0] for i in range(len(fields)))
with open(os.path.join(fpath, head_name), 'w+') as out:
    out.write('\n'.join(str(x) for x in headers))

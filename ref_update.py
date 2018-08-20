# simple script to add ', n' to items that are not of interest
# it is faster to mark only the fields of interest with 'y'
# this script will add 'n' to any fields without 'y'
import os

filepath = os.path.join(os.path.sep, 'Users', 'student', 'nlp', 'clinical_classify')
fname = 'tmp_clinical_items.txt'
outname = 'ref_clinical_items.txt'

contents = []
with open(os.path.join(filepath, fname)) as f:
    for line in f:
        tmp = line.strip().split(',')
        if len(tmp) == 2:
            contents.append(tmp)
        else:
            contents.append([tmp[0], 'n'])

with open(os.path.join(filepath, outname), 'w+') as f:
    f.write('\n'.join(', '.join(str(x) for x in row) for row in contents))

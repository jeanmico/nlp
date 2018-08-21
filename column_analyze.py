import os

fpath = os.path.join(os.path.sep, 'Users', 'student', 'nlp', 'clinical_classify')
fname = 'filtered_data.txt'
fname_head = 'headers.txt'

fpath_out = os.path.join(fpath, 'columns')

data = []
with open(os.path.join(fpath, fname), 'r') as f:
    for line in f:
       tmp = line.strip().split('|')
       data.append(tmp)

headers= ['key']
with open(os.path.join(fpath, fname_head), 'r') as f:
    for line in f:
        headers.append(line.strip())

for i, head in enumerate(headers):
    fname_out = head + '.txt'
    tmp = [data[j][i] for j in range(len(data))]
    with open(os.path.join(fpath_out, fname_out), 'w+') as out:
        out.write('\n'.join(str(x) for x in tmp))


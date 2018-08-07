#INPUT: json file containing all past and current clinical trials
#OUTPUT: two files containing relevant information
# one file includes only current lcinical trials
# one file includes all clinical trials
import os
from bs4 import BeautifulSoup
import json
from pprint import pprint

def print_keys(my_dict):
    if type(my_dict) is dict:
        for k in my_dict.keys():
            print(k)
            print_keys(my_dict[k])
    if type(my_dict) is list:
        for l in my_dict:
            print_keys(l)

fpath = os.path.join(os.path.sep, 'Users', 'student', 'GitHub', 'nlp')
fname = '__data_export.json'
with open(os.path.join(fpath, fname)) as f:
    data = json.load(f)

#pprint(data)

#outfile = 'clinic_parsed.txt'
#with open(os.path.join(fpath, outfile), 'w+') as out:
    #for key, val in data.items():
        #out.write(str(key) + '\t' + str(val))

# only write out the output if the trial is currently visible

# create a separate object with only the current trials visible
print(type(data))
# each key in the dictionary is NCT###..., representing a clinical trial.
print(data['NCT03590054'])
print(type(data['NCT03590054']))
print(data['NCT03590054']['is_visible'])

current_trials = set()
past_trials = set()

for key, val in data.items():
    if val['is_visible'] == True:
        current_trials.add(key)
    elif val['is_visible'] == False:
        past_trials.add(key)

# print number of current and past trials:
print('current trials: ' + str(len(current_trials)))
print('past trials: ' + str(len(past_trials)))

# consider all the keys we have for each trial...
key_data = data['NCT03590054']
print_keys(key_data)

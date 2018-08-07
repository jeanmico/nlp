#INPUT: json file containing all past and current clinical trials
#OUTPUT: two files containing relevant information
# one file includes only current lcinical trials
# one file includes all clinical trials
import os
from bs4 import BeautifulSoup
import json
from pprint import pprint

global key_list
key_list = []

def print_keys(my_dict):
    global key_list
    if type(my_dict) is dict:
        for k in my_dict.keys():
            #print(k)
            key_list.append(k)
            print_keys(my_dict[k])
    if type(my_dict) is list:
        for l in my_dict:
            print_keys(l)

fpath = os.path.join(os.path.sep, 'Users', 'student', 'GitHub', 'nlp')
fname = '__data_export.json'
with open(os.path.join(fpath, fname)) as f:
    data = json.load(f)


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
print(key_list)


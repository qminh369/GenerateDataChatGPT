import json
import pandas as pd 
import re

PATH_SMALL_DATA = 'B:\\TT\\Crawl data\\FakeData\\small_gen_data.txt'
PATH_DATA = 'B:\\TT\\Crawl data\\FakeData\\gen_data.txt'

data = []
with open(PATH_SMALL_DATA, 'r') as file:
    for line in file:
        data.append(line)
        
#print(data)

clean_data = []
text_prompts = []
text_responses = []
text_tasks = []
text_locations = []
text_times = []

remove_strs = ['Certainly', 'Prompt', 'Response', 'Classification', 'These examples', 'Of course', 'Request']

for ele in data:
    ele = re.sub('\n', '', ele)
    ele = re.sub('^Certainly.*', '', ele)
    ele = re.sub('^Prompt.*', '', ele)
    ele = re.sub('^Response.*', '', ele)
    ele = re.sub('^Classification.*', '', ele)
    ele = re.sub('^These examples.*', '', ele)
    ele = re.sub('^Of course.*', '', ele)
    ele = re.sub('^Request: ', '', ele)
    # print(ele)
    if ele != '':
        clean_data.append(ele)
    
#print(clean_data)

for idx in range(len(clean_data)):
    if idx % 4 == 0:
        text_prompts.append(clean_data[idx])
    elif idx % 4 == 1:
        text_tasks.append(clean_data[idx])
    elif idx % 4 == 2:
        text_locations.append(clean_data[idx])
    else:
        text_times.append(clean_data[idx])
        
#print(len(text_prompt))
#print(len(text_task))
#print(len(text_location))
#print(len(text_time))

# print(text_time)

for idx in range(len(text_tasks)):
    text_response = text_tasks[idx] + '\n' + text_locations[idx] + '\n' + text_times[idx]
    text_responses.append(text_response)
    
print(text_responses)    
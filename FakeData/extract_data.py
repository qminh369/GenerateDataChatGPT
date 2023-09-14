import json
import pandas as pd 
import re
import random
import os

def write2json(whole_example=pd.DataFrame([]), gt_task=[]):
    prompts = []
    responses = []

    # Create a DataFrame
    df = pd.DataFrame({
        'prompt': prompts,
        'response': responses,
        'ground truth': gt_task
    })

    # Remove duplicates
    df = df.drop_duplicates()
    if random.randint(0, 9) == 5:
        test_df = df #.drop(index=train_df.index)
        if os.path.exists('B:/TT/Generate Data/FakeData/output/test.jsonl'):
            old_test = pd.read_json('B:/TT/Generate Data/FakeData/output/test.jsonl', orient='records', lines=True)
            pd.concat([old_test, test_df], ignore_index = True).to_json('B:/TT/Generate Data/FakeData/output/test.jsonl', orient='records', lines=True)
        else:
            test_df.to_json('B:/TT/Generate Data/FakeData/output/test.jsonl', orient='records', lines=True)
    # Save the dataframes to .jsonl files
    else:
        train_df = df #.sample(frac=0.9, random_state=42)
        if os.path.exists('./output/train.jsonl'):
            old_train = pd.read_json('./output/train.jsonl', orient='records', lines=True)
            pd.concat([old_train, train_df], ignore_index = True).to_json('B:/TT/Generate Data/FakeData/output/train.jsonl', orient='records', lines=True)
        else:
            train_df.to_json('B:/TT/Generate Data/FakeData/output/train.jsonl', orient='records', lines=True)

PATH_SMALL_DATA = 'B:\\TT\\Generate Data\\FakeData\\small_gen_data.txt'
PATH_DATA = 'B:\\TT\\Generate Data\\FakeData\\gen_data.txt'
PATH_GEN_MISSING_LOCATION_DATA = 'B:\\TT\Generate Data\FakeData\\gen_data_missing_location.txt'
PATH_GEN_MISSING_TIME_DATA = 'B:\\TT\Generate Data\FakeData\\gen_data_missing_time.txt'
PATH_GEN_NEW_FULL_DATA = 'B:\\TT\\Generate Data\\FakeData\\new_full_data.txt'
PATH_GEN_NEW_MISSING_LOCATION_DATA = 'B:\\TT\Generate Data\\FakeData\\new_missing_location.txt'
PATH_GEN_NEW_MISSING_TIME_DATA = 'B:\\TT\\Generate Data\\FakeData\\new_missing_time.txt'

data = []
with open(PATH_GEN_NEW_FULL_DATA, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line)
        
#print(data)

clean_data = []
text_prompts = []
text_responses = []
text_tasks = []
text_locations = []
text_times = []
gt_tasks = []

PATH_GROUND_TRUTH_NEW_FULL_DATA = 'B:\\TT\\Generate Data\\FakeData\\ground_truth_new_full_data.txt'
PATH_GROUND_TRUTH_NEW_MISSING_LOCATION_DATA = 'B:\\TT\Generate Data\\FakeData\\ground_truth_new_missing_location.txt'
PATH_GROUND_TRUTH_NEW_MISSING_TIME_DATA = 'B:\\TT\\Generate Data\\FakeData\\ground_truth_new_missing_time.txt'

with open(PATH_GROUND_TRUTH_NEW_FULL_DATA, 'r', encoding='utf-8') as file:
    for line in file:
        gt_tasks.append(line)

all_tasks = ["calculate Normalized difference vegetation index (NDVI)", "tree counting/detection", "cloud removal from aerial image", "change of building/land/water body detection", "land use/land cover in segmentation", "aircraft category object detection", "car/automobile/four-wheeler/motorcar vehicle like object counting/detection"]

remove_strs = ['Certainly', 'Prompt', 'Response', 'Classification', 'These examples', 'Of course', 'Request: ', 'User Request', 'makefile', 'Copy code', 'vbnet', 'These diverse', 'These prompt/response', 'Sure', 'Prompt: No specific task, location, or time provided.', 'Response: Task: None', 'Location: None', 'Time: None', 'Location: N/A', 'Time: N/A', 'Location: Not specified', 'Time: Not specified' ,'User:', 'Model:']

for ele in data:
    ele = re.sub('\n', '', ele)
    ele = re.sub('["]', '', ele)
    ele = re.sub('^Certainly.*', '', ele)
    #ele = re.sub('^Prompt.*', '', ele)
    ele = re.sub('^Prompt:', '', ele)
    ele = re.sub('^Prompt: ', '', ele)
    ele = re.sub('^A user.*', '', ele)
    ele = re.sub('^ A user.*', '', ele)
    ele = re.sub('^ The user.*', '', ele)
    ele = re.sub('^ A request.*', '', ele)
    ele = re.sub('^Sample.*', '', ele)
    #ele = re.sub('^Response.*', '', ele)
    ele = re.sub('^Response:', '', ele)
    ele = re.sub('^Classification.*', '', ele)
    ele = re.sub('^These examples.*', '', ele)
    #ele = re.sub('^Of course.*', '', ele)
    ele = re.sub('^Request: ', '', ele)
    ele = re.sub('^Request:', '', ele)
    ele = re.sub('^User: ', '', ele)
    ele = re.sub('^User Request: ', '', ele)
    ele = re.sub('^makefile.*', '', ele)
    ele = re.sub('^Copy code.*', '', ele)
    ele = re.sub('^vbnet.*', '', ele)
    ele = re.sub('^These diverse.*', '', ele)
    ele = re.sub('^These prompt/response.*', '', ele)
    #ele = re.sub('^Sure.*', '', ele)
    ele = re.sub('^No specific task, location, or time provided.*', '', ele)
    ele = re.sub('^User: No specific task.*', '', ele)
    ele = re.sub('^Task: None.*', '', ele)
    ele = re.sub('^Location: None.*', '', ele)
    ele = re.sub('^Time: None.*', '', ele)
    ele = re.sub('^Location: N/A.*', '', ele)
    ele = re.sub('^Time: N/A.*', '', ele)
    ele = re.sub('^Location: Not specified.*', '', ele)
    ele = re.sub('^Time: Not specified.*', '', ele)
    ele = re.sub('^These new prompt.*', '', ele)
    ele = re.sub('^These additional prompt.*', '', ele)
    ele = re.sub('^Example.*', '', ele)
    ele = re.sub('^1.*', '', ele)
    ele = re.sub('^2.*', '', ele)
    ele = re.sub('^3.*', '', ele)
    ele = re.sub('^4.*', '', ele)
    ele = re.sub('^5.*', '', ele)
    ele = re.sub('^6.*', '', ele)
    ele = re.sub('^7.*', '', ele)
    ele = re.sub('^8.*', '', ele)
    ele = re.sub('^9.*', '', ele)
    ele = re.sub('^Description: ', '', ele)
    ele = re.sub('^These responses cover various.*', '', ele)
    ele = re.sub('^These responses cover a variety of.*', '', ele)
    ele = re.sub('^These responses cover a range of.*', '', ele)
    ele = re.sub('^These responses encompass various.*', '', ele)
    ele = re.sub('^These responses provide diverse.*', '', ele)
    ele = re.sub('^These samples should provide a diverse.*', '', ele)
    ele = re.sub('^These samples offer a diverse dataset.*', '', ele)
    ele = re.sub('^These samples.*', '', ele)
    ele = re.sub('^Classified Task.*', '', ele)
    ele = re.sub('^These prompts.*', '', ele)
    #ele = re.sub('^Absolutely.*', '', ele)
    ele = re.sub('^No specific task mentioned.*', '', ele)
    ele = re.sub('^Subdistrict.*', '', ele)
    ele = re.sub("^I can generate prompt.*", '', ele)
    ele = re.sub("^Of course, I'll.*", '', ele)
    ele = re.sub("^Of course, I can.*", '', ele)
    ele = re.sub("^Of course, let.*", '', ele)
    ele = re.sub("^Prompt \d:", '', ele)
    ele = re.sub("^Question.*", '', ele)
    ele = re.sub("^Response \d:", '', ele)
    ele = re.sub("^Absolutely, let.*", '', ele)
    ele = re.sub("^Sure, I can help you generate.*", '', ele)
    # print(ele)
    if ele != '':
        clean_data.append(ele)
    
#print(clean_data)

# Generate full data

'''

'''

for idx in range(len(clean_data)):
    if idx % 4 == 0:
        text_prompts.append(clean_data[idx])
    elif idx % 4 == 1:
        text_tasks.append(clean_data[idx])
    elif idx % 4 == 2:
        text_locations.append(clean_data[idx])
    else:
        text_times.append(clean_data[idx])
        
for idx in range(len(text_times)):
    #print(idx)
    text_response = text_tasks[idx] + '\n' + text_locations[idx] + '\n' + text_times[idx]
    text_responses.append(text_response)


# Generate missing location data / Generate missing time data
'''
for idx in range(len(clean_data)):
    if idx % 2 == 0:
        text_prompts.append(clean_data[idx])
    else:
        text_responses.append(clean_data[idx])
'''


   
#print(len(text_prompts))
#print(len(text_responses))
#print(len(text_task))
#print(len(text_location))
#print(len(text_time))

# print(text_time)

#test = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame({
    'prompt': [],
    'response': [],
    'ground truth': []
})


for idx in range(len(gt_tasks)):
    #gt_task = random.choice(all_tasks)
    new_row = {'prompt': text_prompts[idx], 'response': text_responses[idx], 'ground truth': gt_tasks[idx]}
    df = df.append(new_row, ignore_index=True)
    print(idx)

df = df.reset_index(drop=True)
print(df)


#df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\full_data.csv', index=False)
#df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\full_data.jsonl', orient='records', lines=True)

#df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\missing_location_data.csv', index=False)
#df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\missing_location_data.jsonl', orient='records', lines=True)

#df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\missing_time_data.csv', index=False)
#df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\missing_time_data.jsonl', orient='records', lines=True)

df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\new_full_data.csv', index=False)
df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\new_full_data.jsonl', orient='records', lines=True)

#df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\new_missing_location_data.csv', index=False)
#df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\new_missing_location_data.jsonl', orient='records', lines=True)

#df.to_csv('B:\\TT\\Generate Data\\FakeData\\data\\new_missing_time_data.csv', index=False)
#df.to_json('B:\\TT\\Generate Data\\FakeData\\data\\new_missing_time_data.jsonl', orient='records', lines=True)
import json
import os
import glob

def read_json(path):
    data = []
    with open(path) as file:
        for line in file:
            json_line = json.loads(line)
            data.append(json_line)
    # print(len(data))
    return data

def read_prompt(path):
    data_prompt = []
    with open(path) as file:
        for line in file:
            json_line = json.loads(line)
            data_prompt.append(json_line['prompt'])
    # print(len(data))
    return data_prompt
            
def read_response(path):
    data_response = []
    with open(path) as file:
        for line in file:
            json_line = json.loads(line)
            data_response.append(json_line['response'])
    # print(len(data))
    return data_response

def read_ground_truth(path):
    data_ground_truth = []
    with open(path) as file:
        for line in file:
            json_line = json.loads(line)
            data_ground_truth.append(json_line['ground truth'])
    # print(len(data))
    return data_ground_truth

def read_csv(path):
    pass 
        
ROOT_DIR = 'B:\\TT\\Crawl data\\chatGPT\\data'        
        
PATH = 'B:\\TT\\Crawl data\\chatGPT\\data\\1 - full\\train.jsonl'
# print(read_json(PATH))

# print(read_prompt(PATH))
# print(len(read_prompt(PATH)))

#print(read_response(PATH))
#print(len(read_response(PATH)))

#print(read_ground_truth(PATH))
#print(len(read_ground_truth(PATH)))
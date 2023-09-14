import openai
import datetime
import random
from random import randrange
from datetime import timedelta

model = 'text-davinci-003'

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def normalGPT(comment):
    with open('B:\\TT\Generate Data\\FakeData\\general_prompt.txt', 'r') as file:
        general_prompt = file.read()
    response = openai.Completion.create(
        engine = model,
        prompt = general_prompt + comment,
        max_tokens = 48,
        n = 1,
        temperature = 0.5,
    )
    
    return response.choices[0].text


with open('B:\\TT\\Generate Data\\FakeData\\apikey.txt', 'r') as f:
    openai.api_key = f.readline()
    
number_of_examples = 10 # Mất 0.02$

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2023, 9, 8)

PATH_GEN_DATA = 'B:\\TT\Generate Data\FakeData\\gen_data.txt'
PATH_GEN_MISSING_LOCATION_DATA = 'B:\\TT\Generate Data\FakeData\\gen_data_missing_location.txt'
PATH_GEN_MISSING_TIME_DATA = 'B:\\TT\Generate Data\FakeData\\gen_data_missing_time.txt'

for i in range(number_of_examples):
    rand_date = random_date(start_date, end_date).strftime('%d/%m/%Y')
    
    ## Choose task and give use its synonym
    all_task = ["calculate Normalized difference vegetation index (NDVI)", "calculate Normalized difference water index (NDWI)", "calculate Soil-Adjusted Vegetation Index (SAVI)", "tree counting/detection", "cloud removal from aerial image", "change of building/land/water body detection", "land use/land cover in segmentation", "aircraft category object detection", "car/ship/automobile/four-wheeler/motorcar vehicle like object counting/detection", 'none']
    chosen_task = random.choice(all_task[:-1])
    # task_prompt = f'Return synonym of "{chosen_task}" that still keep the origin meaning of object need to identify'
    # use_task = normalGPT(prompt=task_prompt).replace('\n','').lower()
    # print("TASK:",chosen_task, '---' , use_task)

    # Correct
    # prompt = f'A model that takes in a long request with description to perform only "{chosen_task}" task, tasks require location (administrative area ward/commune/subdistrict/town/village level), time (able convert to dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy format, consider today is {rand_date}) to perform. Response will have 3 things: task need to do, location, time and then classify task to one of these {all_task}, location following format: ward/district/city/province/country, time following format: dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy. Give response in format "Task:...\nLocation:...\nTime:..."'
    # prompt = f'A model that takes in a long question with description to perform "{chosen_task}", tasks require location (administrative area ward/commune/subdistrict/town/village level), time (able convert to format dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy, consider today is {rand_date}) to perform. Relative time is accepted for example: today, last month, previous summer,..., but location will not given or not following format so ask for specific location in response to retrieve it, do not say anything else'
    prompt = f'A model that takes in a long request with description to perform "{chosen_task}" task , tasks require location (administrative area ward/commune/subdistrict/town/village level, most likely in India, Vietnam, Thailand, Singapore, Indonesia), time (able convert to format dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy, consider today is {rand_date}) to perform. Location is provide but time will not given or not able convert to right format in input prompt so ask in response to retrieve it'
    result = normalGPT(prompt)
    with open(PATH_GEN_MISSING_TIME_DATA , 'a', encoding = 'utf-8') as file:
        file.write(result + '\n')

    
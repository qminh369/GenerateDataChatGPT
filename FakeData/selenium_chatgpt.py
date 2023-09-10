from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium import webdriver
import os
import time
import json
from random import randrange
import random
from datetime import timedelta
import pandas as pd
import tqdm
import datetime
#from read_data import *


# Thư viện undetected_chromedriver để vượt captcha
chrome_options = Options()
driver = uc.Chrome(chrome_options=chrome_options)

'''
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-extensions")

# Phải tải lại chrome driver mỗi lần update
chrome_driver_path = 'B:\\Sentiment Analysis\\chromedriver-win32\\chromedriver.exe'
chrome_service = Service(chrome_driver_path, options = chrome_options)
driver = webdriver.Chrome(service=chrome_service)
'''

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def write2json(example=pd.DataFrame([]), gt_task=[]):
    prompts = []
    responses = []

    # Parse out prompts and responses from examples
    split_example = example.split('-----------') if len(example.split('-----------')) == 4 else example.split('-----------')[:-1]  #[:-1]
    if len(split_example) != 4:
            raise Exception("Output format is not assert, expected length 4 but got length of {}.".format(len(split_example)))

    prompts.append(split_example[1].strip())
    responses.append(split_example[3].strip())

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
        if os.path.exists('./output/test.jsonl'):
            old_test = pd.read_json('./output/test.jsonl', orient='records', lines=True)
            pd.concat([old_test, test_df], ignore_index = True).to_json('./output/test.jsonl', orient='records', lines=True)
        else:
            test_df.to_json('./output/test.jsonl', orient='records', lines=True)
    # Save the dataframes to .jsonl files
    else:
        train_df = df #.sample(frac=0.9, random_state=42)
        if os.path.exists('./output/train.jsonl'):
            old_train = pd.read_json('./output/train.jsonl', orient='records', lines=True)
            pd.concat([old_train, train_df], ignore_index = True).to_json('./output/train.jsonl', orient='records', lines=True)
        else:
            train_df.to_json('./output/train.jsonl', orient='records', lines=True)

os.makedirs('./output', exist_ok=True)

'''
# (code cũ) Nhập prompt
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\prompt_aspect.txt', 'r', encoding = 'utf-8') as file:
    prompt = file.read()
    
with open('B:\\Đồ án I\\Project I\\selenium automatic chatgpt\\comment.txt', 'r', encoding='utf-8') as file:
    comments = []
    for line in file:
        comments.append(line)

summarize = []
for i in range(0, len(comments)-5, 5):
    summarize.append(comments[i] + comments[i+1] + comments[i+2] + comments[i+3] + comments[i+4])
'''


# Mở trang web ChatGPT
driver.get('https://chat.openai.com/auth/login')
time.sleep(3)

# Đăng nhập tài khoản chatgpt
button_login = driver.find_element(By.XPATH, "//div[@class='relative -top-[1px]']")
button_login.click()
time.sleep(3)

accounts = ['quangminhpulisic123@gmail.com', 'niallerjamespotter@gmail.com', 'phanan1227@gmail.com', 'tungteng0401@gmail.com', 'sktblank2212@gmail.com']
passwords = ['minhboy123', '12345678', 'phanlacan12', '@jTtM*wUvT4B62.', 'minhkepa2212']

idx_rand = randrange(0, len(accounts))

# Nhập tài khoản, mật khẩu
mail = driver.find_elements(By.TAG_NAME, "input")[1]
mail.send_keys(accounts[idx_rand])
btn = driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

pw = driver.find_elements(By.TAG_NAME,"input")[2]
pw.send_keys(passwords[idx_rand])

# Button continue
btn = driver.find_element(By.XPATH, "//button[@class = 'ca796cae5 c07e204b0 c6990c4ce cba7675b8 _button-login-password']")
btn.click()
time.sleep(2)

#time.sleep(30)
# 3 Button sau đó
btn1 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-primary']")
btn1.click()
'''
time.sleep(2)
btn2 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-neutral ml-auto']")
btn2.click()
time.sleep(2)
btn3 = driver.find_element(By.XPATH, "//button[@class = 'btn relative btn-primary ml-auto']")
btn3.click()
time.sleep(2)
'''

'''
for i in range(3):
    text_area = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = arguments[1];", text_area, prompt + summarize[i])
    text_area.send_keys(Keys.ENTER)

    btn_answer = driver.find_element(By.XPATH, "//button[@class = 'absolute p-1 rounded-md md:bottom-3 md:p-2 md:right-3 dark:hover:bg-gray-900 dark:disabled:hover:bg-transparent right-2 disabled:text-gray-400 enabled:bg-brand-purple text-white bottom-1.5 transition-colors disabled:opacity-40']")
    btn_answer.click()
    time.sleep(30)
    
    answer = driver.find_elements(By.XPATH, "//div[@class = 'markdown prose w-full break-words dark:prose-invert light']")[i]
    result = answer.text
    print(result)

    with open('B:\\TT\Crawl data\\FakeData\\text.txt', 'a', encoding = 'utf-8') as file:
        file.write(result + '\n')

    time.sleep(5)
'''

with open('B:\\TT\Crawl data\\FakeData\\general_prompt.txt', 'r') as file:
    general_prompt = file.read()

number_of_examples = 100

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2023, 9, 8)

for i in range(number_of_examples):
    rand_date = random_date(start_date, end_date).strftime('%d/%m/%Y')
    
    ## Choose task and give use its synonym
    all_task = ["calculate Normalized difference vegetation index (NDVI)", "tree counting/detection", "cloud removal from aerial image", "change of building/land/water body detection", "land use/land cover in segmentation", "aircraft category object detection", "car/automobile/four-wheeler/motorcar vehicle like object counting/detection", 'none']
    chosen_task = random.choice(all_task[:-1])
    # task_prompt = f'Return synonym of "{chosen_task}" that still keep the origin meaning of object need to identify'
    # use_task = normalGPT(prompt=task_prompt).replace('\n','').lower()
    # print("TASK:",chosen_task, '---' , use_task)

    # Correct
    prompt = f'A model that takes in a long request with description to perform only "{chosen_task}" task, tasks require location (administrative area ward/commune/subdistrict/town/village level), time (able convert to dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy format, consider today is {rand_date}) to perform. Response will have 3 things: task need to do, location, time and then classify task to one of these {all_task}, location following format: ward/district/city/province/country, time following format: dd/mm/yyyy or dd/mm/yyyy-dd/mm/yyyy. Give response in format "Task:...\nLocation:...\nTime:..."'
    
    # Interact chatgpt
    text_area = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = arguments[1];", text_area, general_prompt + prompt)
    text_area.send_keys(Keys.ENTER)

    btn_answer = driver.find_element(By.XPATH, "//button[@class = 'absolute p-1 rounded-md md:bottom-3 md:p-2 md:right-3 dark:hover:bg-gray-900 dark:disabled:hover:bg-transparent right-2 disabled:text-gray-400 enabled:bg-brand-purple text-white bottom-1.5 transition-colors disabled:opacity-40']")
    btn_answer.click()
    time.sleep(30)
    
    answer = driver.find_elements(By.XPATH, "//div[@class = 'markdown prose w-full break-words dark:prose-invert light']")[i]
    result = answer.text
    print(result)

    with open('B:\\TT\Crawl data\\FakeData\\gen_data.txt', 'a', encoding = 'utf-8') as file:
        file.write(result + '\n')

    time.sleep(5)

driver.quit()
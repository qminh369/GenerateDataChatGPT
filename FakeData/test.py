import undetected_chromedriver as uc
from random import randrange
from datetime import timedelta
import datetime
import random
print(uc.__version__)

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2023, 9, 8)

#print(random_date(start_date,end_date))

text = "I have a task for you that requires you to use aerial images from the T\u00e2n B\u00ecnh Ward, S\u01a1n Tr\u00e0 District, \u0110\u00e0 N\u1eb5ng City, Vietnam"
# print(text)

with open('B:\\TT\Generate Data\\FakeData\\general_prompt.txt', 'r') as file:
    general_prompt = file.read()
    
# print(general_prompt)

#rand = randrange(0, 4)
#print(rand)

with open('B:\\TT\Generate Data\\FakeData\\small_gen_data.txt', 'r') as file:
    small_gen_data = file.read()
    
all_task = ["calculate Normalized difference vegetation index (NDVI)", "calculate Normalized difference water index (NDWI)", "calculate Soil-Adjusted Vegetation Index (SAVI)", "tree counting/detection", "cloud removal from aerial image", "change of building/land/water body detection", "land use/land cover in segmentation", "aircraft category object detection", "car/ship/automobile/four-wheeler/motorcar vehicle like object counting/detection", 'none']
chosen_task = random.choice(all_task[:-1])
print(chosen_task)
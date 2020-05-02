import time
from functools import wraps
from csv import writer


def image_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        tmp_time = t1 - t0
        arr = [tmp_time]
        append_list_as_row('measurements/log_image.csv', arr)
        return result
    return function_timer


def speech_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        tmp_time = t1 - t0
        arr = [tmp_time]
        append_list_as_row('measurements/log_speech.csv', arr)
        return result
    return function_timer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

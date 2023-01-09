import string
import random
import time

def time_float_to_str(time_float_value: float):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time_float_value))
from functools import wraps
from time import time

def measure(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end = int(round(time() * 1000)) - start
            print(f"Total execution time: {end} ms")
    return time_it





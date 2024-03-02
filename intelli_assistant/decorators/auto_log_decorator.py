import logging
import functools
import os

def auto_log(log_file='app.log', log_result=False):
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, log_file)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
            logging.info(f"{func.__name__} called with {args}, {kwargs}")
            result = func(*args, **kwargs)
            if log_result:
                logging.info(f"{func.__name__} returned: {result}")
            return result
        return wrapper
    return decorator

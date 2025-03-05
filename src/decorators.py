import logging
from functools import wraps
from datetime import datetime

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # Если filename указан, настраиваем логгер для записи в файл
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()
        return wrapper
    return decorator

# import time
from celery import Celery
from pymongo import MongoClient
# from celery.utils.log import get_task_logger

# logger = get_task_logger(__name__)

app = Celery('cel',
             broker='amqp://admin:admin@rabbit:5672',
             backend='rpc://')

# @app.task()
# def longtime_add(x, y):
#     logger.info('Got Request - Starting work ')
#     time.sleep(4)
#     logger.info('Work Finished ')
#     return x + y

@app.task(name='cel.print_str')
def print_str(a_string):
    return "Returned string: " + a_string

@app.task(name='cel.test')
def test():
    return 'This is a test celery task!'

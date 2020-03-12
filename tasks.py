
# #broker='sqs://AKIARJLDNDHBUNFR7PVK:lWpWXK91cRaKkFJwoCzO6tE24XhfdQEsfT8Gzj57@'
# redis='redis://localhost:6379'
# app = Celery('tasks', backend=redis, broker=redis)
# app.config_from_object('celeryconfig')

# from __future__ import absolute_import, unicode_literals
#from celery import app

#from celery import Celery

#app = Celery('proj', broker=redis, backend=redis)
#app.config_from_object('celeryconfig')

from __future__ import absolute_import, unicode_literals

from .celery import app


@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)

#
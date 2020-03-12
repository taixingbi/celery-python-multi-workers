from __future__ import absolute_import, unicode_literals

from celery import Celery
#app.config_from_object('celeryconfig')
redis='redis://localhost:6379'


app = Celery('proj',
             broker=redis,
             backend=redis,
             include=['proj.tasks'])

app.conf.update(
    result_expires=3600,
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

if __name__ == '__main__':
    app.start()


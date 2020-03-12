
redis='redis://localhost:6379'

broker_url = redis
result_backend = redis

result_expires=3600


task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']


timezone = 'Europe/Oslo'
enable_utc = True

task_routes = {
    'tasks.add': 'low-priority',
}

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}



### run pip shell
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### start redis
```
docker run -d -p 6379:6379 redis
```

### config
```
python -m celeryconfig
```

### cmd
```
from tasks import add
result= add.delay(2, 4)

from tasks import mul
result= mul.delay(2, 14)


result.ready()
result.status
result.get()
```

###

celery multi start w1 -A proj -l info
celery multi restart w1 -A proj -l info
celery multi stop w1 -A proj -l info






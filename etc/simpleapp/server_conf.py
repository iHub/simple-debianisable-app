import multiprocessing


bind = '127.0.0.1:24312'
workers = multiprocessing.cpu_count() * 2 + 1
user = "simpleapp"
group = "simpleapp"

errorlog = '/var/log/simpleapp/gunicorn.error.log'
loglevel = 'debug'
accesslog = '/var/log/simpleapp/gunicorn.access.log'

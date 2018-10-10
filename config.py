import os

class Config(object):
    REDISLITE_PATH = os.environ.get('REDISLITE_PATH') or '/dev/shm/sign.rdb'

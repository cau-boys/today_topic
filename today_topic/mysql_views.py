from djnago.db import connections

def make_connection():
    db_type = 'default'
    cursor = connections[db_type].cursor()
    return cursor

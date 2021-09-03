import os

home = os.path.expanduser('~')

def to_table(obj):
    if type(obj) is not dict:
        raise TypeError()

    return ''.join(['{} {}\n'.format(key, value) for key, value in obj.items()])
import os

home = os.path.expanduser('~')

def to_table(obj):
    if type(obj) is not dict:
        raise TypeError()

    return ''.join(['{} {}\n'.format(key, value) for key, value in obj.items()])

def dict_to_csv(obj, header=None):
    if type(obj) is not dict:
        print(type(obj))
        raise TypeError()

    csv = ''.join(['{},{}\n'.format(key, value) for key, value in obj.items()])

    return csv if header is None else '{},{}\n'.format(header[0], header[1]) + csv
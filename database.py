from msilib.schema import Error
import os

class Database:
    def __init__(self, path):
        if os.path.exists(path):
            _validate(path)

        if path[-3:] != '.db':
            path += '.db'

        self.path = path
        self.database = open(path, 'a')
        self.data = None

        if os.path.exists(path):
            self.data = _extract(path)
        else:
            self.data = dict()

    def push(self, key, value):
        if key in self.data:
            return False
        
        self.data[key] = value
        self.database.write(f'{key}>>{value}::')

        return True
    
    def fetch(self, key):
        if key in self.data:
            return self.data[key]
        return None
    
    def reset(self):
        self.data = dict()
        self.database = open(self.path, 'w')
        self.database.write('')

    def close(self):
        self.database.close()
    
    def get_path(self):
        return os.path.basename(self.path)

    def size(self):
        return len(self.data)

def _extract(path):
    to_return = dict()
    db = open(path, 'r')
    
    for line in db:
        elements = line.split('::')[:-1]

        for e in elements:
            key = e.split('>>')[0]
            val = e.split('>>')[1]
            to_return[key] = val
    
    return to_return

def _validate(path):

    if path == '.db':
        raise ValueError(f'File must have name')
        
    _, ext = os.path.splitext(path)

    if ext != '' and ext != '.db':
        raise ValueError(f'Invalid file format')
    
    file = open(path, 'r')
    
    lines = file.readlines()

    if len(lines) > 1:
        raise ValueError('Unable to parse file')
    
    if len(lines) == 0:
        return
    
    line = lines[0]

    try:
        if '::' not in line and '>>' not in line:
            raise Error
        for e in line.split('::')[:-1]:
            key = e.split('>>')[0]
            val = e.split('>>')[1]
        return
    except:
        raise ValueError('Unable to parse file')





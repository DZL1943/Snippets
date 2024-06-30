import os
from pprint import pprint as print

def list_files(startpath):
    result = []
    for entry in os.scandir(startpath):
        if entry.is_file():
            result.append({'name': entry.name, 'path': entry.path, 'is_file': True})
        elif entry.is_dir():
            children = list_files(entry.path)
            result.append({'name': entry.name, 'path': entry.path, 'is_file': False, 'children': children})
    return result

# Example usage:
files_list = list_files('/users/mac/tmp')
print(files_list)
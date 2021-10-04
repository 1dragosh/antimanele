# -*- coding: utf-8 -*-

# Author: 1dragosh

import os
import platform
import unidecode
import requests

data = requests.get('https://1dragosh.github.io/manelisti.txt').text

manelisti = [x for x in data.split("\n") if len(x) > 2]

if platform.system() == 'Windows':
    delimiter = '\\'
else:
    delimiter = '/'

root = '.{}'.format(delimiter)

filepath = []

for path, _, files in os.walk(root):
    filepath.extend([os.path.join(path, file).replace('\\', delimiter).replace('/', delimiter) for file in files
                     if str(file).endswith('.mp3')])

for fle in filepath:
    file_name = unidecode.unidecode(str(fle.split(delimiter)[-1].split('.')[0])).lower()
    for _ in file_name.split():
        if _ in manelisti:
            os.remove(fle)
            break

    for _ in file_name.split('-'):
        if _ in manelisti:
            os.remove(fle)
            break

    for _ in file_name.split('_'):
        if _ in manelisti:
            os.remove(fle)
            break

    for _ in file_name.split('.'):
        if _ in manelisti:
            os.remove(fle)
            break

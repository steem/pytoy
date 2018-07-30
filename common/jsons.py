import json
import os

def from_file(file_path, **kwargs):
  if not os.path.isfile(file_path):
    return None
  with open(file_path, encoding='utf-8') as f:
    return json.load(f, **kwargs)

def to_file(file_path, dict):
  with open(file_path, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(dict))

def from_txt_file(file_path, sep = "\n", key_sep = None, encoding='utf-8'):
  if not os.path.isfile(file_path):
    return None
  with open(file_path, encoding = encoding) as f:
    ds = f.read()
    ds = ds.split(sep)
    if key_sep is None:
      data = []
      for d in ds:
        data.append(d)
      return data
    data = {}
    for d in ds:
      d = d.split(key_sep)
      data[d[0]] = d[1]
    return data 
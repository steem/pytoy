import os
import sys

CUR_DIR = os.path.dirname(sys.argv[0]) if os.path.isabs(sys.argv[0]) else sys.path[0]
CUR_DIR_NAME = os.path.basename(CUR_DIR)
COMMON = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(COMMON)
DATA = ROOT + os.sep + 'data'
LOGS = ROOT + os.sep + 'logs'
CFG_DIR = ROOT + os.sep + 'config'
MAIN_CFG = CFG_DIR + os.sep + 'config.json'
MACHINE_CFG = CFG_DIR + os.sep + 'config_machine.json'
SELF_CFG = CFG_DIR + os.sep + 'config_self.json'

def cfg_file(sub_dir):
  return {
    'MAIN_CFG' : os.path.join(ROOT, 'config', sub_dir, 'config.json'),
    'MACHINE_CFG' : os.path.join(ROOT, 'config', sub_dir, 'config_machine.json'),
    'SELF_CFG' : os.path.join(ROOT, 'config', sub_dir, 'config_self.json'),
  }

def create_dirs(dirs):
  if not isinstance(dirs, list):
    dirs = [dirs]
  for dir in dirs:
    if not os.path.isdir(dir):
      os.mkdir(dir)

def all_files_exists(files):
  for file in files:
    if not os.path.isfile(file):
      return False
  return True

def del_file(p):
  if os.path.isfile(p):
    os.remove(p)

def all_dirs_exists(dirs):
  for dir in dirs:
    if not os.path.isdir(dir):
      return False
  return True

def touch(path):
    if not path:
        return
    path = os.path.realpath(path)
    if path.find("/") > 0 and not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    try:
        os.utime(path, None)
    except Exception:
        open(path, 'a').close()
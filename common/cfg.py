import os
from . import logger, jsons, paths
import json

_cfg = {}
_last_load_times = {}
log = logger.get()

__all__ = [
  'C',
  'load',
]

def C(name, default = None):
  return _cfg.get(name, default)

def _load_internal(file_path, force = False):
  if not os.path.isfile(file_path):
    return None
  
  t = os.path.getmtime(file_path)
  o = _last_load_times.get(file_path) if _last_load_times.get(file_path) is not None else 0
  if not force and t == o:
    return None
  _last_load_times[file_path] = t
  d = jsons.from_file(file_path)
  log.info('Load config file: ' + file_path + ', new config: ' + json.dumps(d))
  return d

def load():
  new_cfg = {}

  tmp_cfg = _load_internal(paths.MAIN_CFG)
  if tmp_cfg is not None:
    new_cfg.update(tmp_cfg)
  tmp_cfg = _load_internal(paths.MACHINE_CFG)
  if tmp_cfg is not None:
    new_cfg.update(tmp_cfg)
  tmp_cfg = _load_internal(paths.SELF_CFG)
  if tmp_cfg is not None:
    new_cfg.update(tmp_cfg)
 
  if os.path.isdir(paths.CFG_DIR + os.sep + paths.CUR_DIR_NAME):
    p = paths.cfg_file(paths.CUR_DIR_NAME)
    tmp_cfg = _load_internal(p['MAIN_CFG'])
    if tmp_cfg is not None:
      new_cfg.update(tmp_cfg)
    tmp_cfg = _load_internal(p['MACHINE_CFG'])
    if tmp_cfg is not None:
      new_cfg.update(tmp_cfg)
    tmp_cfg = _load_internal(p['SELF_CFG'])
    if tmp_cfg is not None:
      new_cfg.update(tmp_cfg)
  if len(new_cfg) > 0:
    _cfg.update(new_cfg)

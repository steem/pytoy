import logging
import logging.config
from . import jsons, paths
from . import cmdline as cli
import os
import sys

_logger = None
_dir = os.path.dirname(os.path.abspath(__file__))
_parent_dir = os.path.dirname(_dir)

def _get_log_file():
  log_dir = _parent_dir + os.sep + 'logs'
  if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
  name = os.path.splitext(os.path.basename(sys.argv[0]))[0] + cli.A('-type', "", "_")
  return log_dir + os.sep + os.path.basename(paths.CUR_DIR) + '.' + name + '.log'

def _init():
  global _logger
  
  cli.init_arguments()
  log_file = _get_log_file()
  config_file = _parent_dir + os.sep + "log.json"
  logging.basicConfig(format = '%(asctime)s [%(levelname)s] %(message)s (at %(pathname)s:%(lineno)d)',
                  datefmt = '%Y-%m-%d %H:%M:%S',
                  filename = log_file)
  _logger = logging.getLogger()
  _logger.setLevel(logging.DEBUG)
  config = jsons.from_file(config_file)
  if config:
    logging.config.dictConfig(config)

def get():
  if _logger is None:
    _init()
  return _logger

__all__ = ['get']
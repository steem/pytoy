
import sys
import os
PP_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(PP_ROOT))
from common import apps, paths, cfg, jsons, logger

log = logger.get()

class SampleApp:
  def get_dirs(self):
    return []
  
  def initialize(self):
    print('init')
    print(jsons.from_txt_file(os.path.join(PP_ROOT, 'test.txt'), key_sep = '='))
    log.info('init')

  def run(self):
    print('run')

  def cleanup(self):
    print('cleanup')

if __name__ == '__main__':
  apps.run(SampleApp())

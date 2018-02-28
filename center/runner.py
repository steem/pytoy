import sys
import os
PP_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(PP_ROOT))
from common import proc, paths, cfg
from common import cmdline as cli

cli.init_arguments()
cfg.load()

targets = [

]

for i, target in enumerate(targets):
  targets[i] = paths.COMMON + os.sep + 'monitor.py -file=' + PP_ROOT + os.sep + target

proc.daemon(targets)

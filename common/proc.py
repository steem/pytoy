import subprocess
import platform
from . import logger

is_windows = True if platform.system() == "Windows" else False

def daemon(cmds, executor = 'python'):
  log = logger.get()
  if not isinstance(cmds, list):
    cmds = [cmds]
  if cmds.__len__() == 0:
    print('No commands to be executing')
    return
  shell = True if is_windows else False
  for cmd in cmds:
    cmd = executor + ' ' + cmd
    log.warn(cmd)
    subprocess.Popen(cmd, shell = shell)

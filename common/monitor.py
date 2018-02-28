import sys
import os
import time
import cmdline as cli

def monitor():
  cli.init_arguments()
  executor = cli.A('-cmd')
  file = cli.A('-file')
  if executor is None and file is None:
    print('Nothing to be executed')
    return
  if executor is None:
    executor = 'python ' + file
  else:
    if os.path.isfile(executor):
      file = executor
    else:
      file = sys.argv[2] if sys.argv.__len__() > 2 else ''
  if not os.path.isfile(file):
    print('Execution file(%s) does not exist' % (file))
    return
  args = ''
  for i in range(2, sys.argv.__len__() - 1):
    args += ' ' + sys.argv[i]
  env = cli.A('-bind_ip', '')
  if env.__len__() > 0:
    env = "BIND_ADDR='" + env + "' LD_PRELOAD='/usr/lib/bind.so "
  cmd = env + executor + args
  file += '.stop'
  while True:
    os.system(cmd)
    if os.path.isfile(file):
      print('Stoped: ' + file)
      os.unlink(file)
      break
    time.sleep(1)

if __name__ == "__main__":
  monitor()

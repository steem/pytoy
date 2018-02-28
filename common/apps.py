import time
import sys
from . import cfg, paths, logger
from . import cmdline as cli

def run(app):
  cli.init_arguments()
  cfg.load()
  log = logger.get()
  if hasattr(app, 'get_dirs'):
    paths.create_dirs(app.get_dirs())
  if hasattr(app, 'initialize'):
    if app.initialize() == False:
      log.warn('Failed to initialize')
      return
    log.info('App is initialized')
  has_sleep = True if hasattr(app, 'sleep') else False
  while (True):
    try:
      cfg.load()
      if app.run() == False:
        break
      if has_sleep:
        app.sleep()
      else:
        time.sleep(1)
    except KeyboardInterrupt:
      break
    except:
      log.warn(sys.exc_info()[0] + ' ' + sys.exc_info()[1])
      break
  if hasattr(app, 'cleanup'):
    try:
      app.cleanup()
    except KeyboardInterrupt:
      pass
    except:
      log.warn(sys.exc_info()[0] + ' ' + sys.exc_info()[1])
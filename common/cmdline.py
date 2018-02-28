import sys

args = {}
def init_arguments():
  if args.get('__inited__') is not None:
    return
  for arg in sys.argv:
      item = arg.split('=', 1)
      if item.__len__() < 2:
        continue
      args[item[0]] = item[1]
  args['__inited__'] = True

def A(name, default = None, prepend = "", append = ""):
  return prepend + args[name] + append if args.get(name) is not None else default

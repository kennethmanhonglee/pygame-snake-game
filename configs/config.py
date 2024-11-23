import yaml
from easydict import EasyDict as edict
from functools import reduce
from operator import getitem

class Config:
  def __init__(self):
    with open('configs/config.yaml', 'r') as config_file:
      self.configs = edict(yaml.safe_load(config_file))

  def get(self, config_str):
    '''
    :param1 config_str: a dot(.) separated string of keys to access configs

    reduce - like JS reduce, it takes 3 arguments:
      1. function to be called
      2. iterable to be iterated over, and passed to the function
      3. initial item
      reduce will take the initial (if given, if not then use first iterable)
      call the function from param1, and pass in both the initial and current iterable
      whatever is returned is used as the initial for the next iteration

      here, getitem(a, b) returns a[b]
      we will start with a dict of configs, and iterate over the keys needed and
      call getitem to call it on self.configs
    '''
    config_keys = config_str.split('.')
    return reduce(getitem, config_keys, self.configs)

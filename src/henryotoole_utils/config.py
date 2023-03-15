# henryotoole_utils/config.py
# Josh Reed 2020
#
# A utility to assist with the loading of config files

# Base python
import os
import types
import time

def load_config(config_path):
	"""Load a config file into memory from a path.

	Args:
		config_path (string): The absolute path to the config file.

	Returns:
		dict: the config file with key/value pairs in a dict.
	"""



	# https://github.com/pallets/flask/blob/master/src/flask/config.py
	d = types.ModuleType("config")
	d.__file__ = config_path

	# Honestly I've no idea how the below works - I copied it from the Flask source code.
	with open(config_path, mode="rb") as config_file:
		exec(compile(config_file.read(), config_path, "exec"), d.__dict__)
	
	ret_config = {}

	# This unpacks the ModuleType somehow?
	for key in dir(d):
		if key.isupper():
			ret_config[key] = getattr(d, key)
	return ret_config
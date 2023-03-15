# henryotoole_utils/flask.py
# Josh Reed 2020
#
# A set of functions and decorators that supplement a flask server.

from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
	"""
	A simple decorator which can be used to add headers to a flask response which will tell the browser to not cache
	the results (ever!). Credit to Armin Ronacher and Aru Sahni for the core snippet which informed this snippet.
	https://arusahni.net/blog/2014/03/flask-nocache.html
	
	WARNING: This has not been tested with flask_gpq and might break it

	Args:
		view (function): The flask routed function we wish to anticache
	"""
	@wraps(view)
	def no_cache(*args, **kwargs):
		response = make_response(view(*args, **kwargs))
		response.headers['Last-Modified'] = datetime.now()
		response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
		response.headers['Pragma'] = 'no-cache'
		response.headers['Expires'] = '-1'
		return response
		
	return update_wrapper(no_cache, view)
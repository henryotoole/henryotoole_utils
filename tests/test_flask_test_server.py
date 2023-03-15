# henryotoole_utils/tests/t_flask_test_server.py
# Josh Reed 2020
#
# This is a pretty rudimentary test file to make sure the flask test server
# and associated test client basically works.

# FOR NOW we are going to use sys.path.insert here. When I get around to actually
# releasing dispatch and henryotoole_utils, I'll need to remove this and use 'pip install -e .'
# This will require giving both hutils and dispatch their own venv's...
# https://stackoverflow.com/questions/50155464/using-pytest-with-a-src-layer
# https://stackoverflow.com/questions/53378416/what-does-pipenv-install-e-do-and-how-to-use-it?noredirect=1&lq=1
import sys
sys.path.insert(0, "/the_root/projects/code_projects/henryotoole_utils/src")

# Our imports
from henryotoole_utils.flask_test_server import FlaskTestServer, FlaskTestClient, FlaskAppRouteTestBlock
from henryotoole_utils.flask_sample_test_app import FlaskUser

# Other libraries
import pytest

# Base imports
import time


base_url = 'http://localhost'
base_url_port = base_url + ":5000"

@pytest.fixture
def test_flask_app():
	"""Create a fixture which represents the flask test server running a flask app

	Yields:
		FlaskTestServer: A flask app instance
	"""

	import henryotoole_utils.flask_sample_test_app
	from henryotoole_utils.flask_sample_test_app import app

	test_server = FlaskTestServer()
	test_server.setup_dev_server(app, base_url)

	yield test_server

	test_server.dev_server_stop()


def test_server_interact(test_flask_app):
	"""Make sure we can send requests to the server
	"""

	client = FlaskTestClient(base_url_port)
	client.login_user('/login_login', FlaskUser.USER_EMAIL, FlaskUser.USER_PASS)

	block = FlaskAppRouteTestBlock(
		'/test_route',
		200,
		{'key': 'val'},
		request_data={'test_param': 'hello'}
	)

	client.assert_block(block)

	block = FlaskAppRouteTestBlock(
		'/test_login',
		200,
		{}
	)

	client.assert_block(block)
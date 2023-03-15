# henryotoole_utils/flask_sample_test_server.py
# Josh Reed 2021
#
# This is a sample flask server with very basic routes which is used to test the flask
# test server functionality of this library.
#
# To use this, flask and flask_login must be installed and venv'd properly

import flask
import flask_login
from flask import Flask, jsonify, request
from flask_login import login_user, login_required

#Sets up the extensions and other path-containing files in this module
def setup():

	app.secret_key = b'aleksandr_solzhenitsyn'
	
	register_login(app)
	add_routes(app)
	

#We register extensions in this way to prevent circular import references. Simply provides a
#reference to 'app' to each extension.
def register_login(app):

	# Setup the login module
	login_manager = flask_login.LoginManager()
	login_manager.login_view = "login"
	login_manager.init_app(app)

	# Add the user loader function
	@login_manager.user_loader
	def load_user(user_id):
		return FlaskUser(user_id)

def add_routes(app):
	"""Add some routes for testing.
	"""

	# Register the login route
	@app.route('/login_login', methods=['GET', 'POST'])
	def login_login():
		email = request.values.get('email', type=str)
		password = request.values.get('password', type=str)
		if(email == FlaskUser.USER_EMAIL and password == FlaskUser.USER_PASS):
			user = FlaskUser(FlaskUser.USER_ID)
			login_user(user)
			return "", 200
		return "Bad login credentials", 403

	@app.route('/test_route', methods=['GET', 'POST'])
	def test_route():
		test_param = request.values.get('test_param', type=str)

		if(test_param == 'hello'):
			return jsonify({'key': 'val'}), 200
		else:
			return "did not say hello", 404

	@app.route('/test_login', methods=['GET', 'POST'])
	@login_required
	def test_login():
		return jsonify({}), 200



#This code is called whenever the module is imported
app = Flask(__name__)
setup()

class FlaskUser:

	USER_ID = 1
	USER_EMAIL = 'test_email'
	USER_PASS = 'test_pass'

	is_anonymous = False

	def __init__(self, user_id):
		"""Create a dummy flask user. For this server, there's only one user and it has
		a constant username and password.
		"""
		self.user_id = user_id

	def is_authenticated(self):
		return self.user_id == FlaskUser.USER_ID

	def is_active(self):
		return True
	
	def get_id(self):
		return self.user_id
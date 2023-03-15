# henryotoole_utils/db.py
# Josh Reed 2020
#
# Some helper code for managing sqlalchemy databases (similar to how flask_db does it)

# Our own code

# Other libraries
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base python

class Database():

	def __init__(self, db_uri):
		"""Instantiate a database session/engine pair which can be used consistently to 
		interact with a database.

		Args:
			db_uri (String): the database string like 'mysql+pymysql://root:mysql_password@localhost/grid332'
		"""
		self.engine = create_engine(db_uri)
		self.model_base = declarative_base()

		# https://stackoverflow.com/questions/20201809/sqlalchemy-flask-attributeerror-session-object-has-no-attribute-model-chan
		Session = sessionmaker(bind=self.engine)
		session = Session()
		session._model_changes = {}
		self.session = session
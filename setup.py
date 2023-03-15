# henryotoole_utils/setup.py
# Josh Reed 2020
#
# This sets up the henryotoole utility module system wide. To install it run
# >> python setup.py install
from glob import glob

import setuptools
from setuptools import setup
from setuptools import find_packages

# Changelog:
# 0.0.1
#	This was the base creation of this utility
# 0.0.2
#	This adds the flask_test_server and tests for that test server.
# 0.1.0
# 	Improved setup.py

setup(
	name="henryotoole_utils",
	packages=find_packages('src'),
	package_dir={'': 'src'},
	version='0.1.0',
	license='GNUv3',
	description='Really basic utils for my fleet of code.',
	author='Josh Reed (henryotoole)',
	py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
)
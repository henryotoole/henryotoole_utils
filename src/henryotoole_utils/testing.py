# henryotoole_util/util_tests.py
# Josh Reed 2020
#
# Test script decorator

import functools
import traceback

# Note that anything decorated with this function should take no arguments and return True or False
# to indicate whether the test succeeded or failed.
def test_function(module_name, object_name):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapped_function(*args, **kwargs):
			return func(*args, **kwargs)

		# register this test function
		test_extension.register_test_function(
			wrapped_function,
			module_name,
			object_name,
			func.__name__
		)

		return wrapped_function
	return decorator_repeat

class TestExtension():

	def __init__(self):
		"""Initialize the test infrastructure.
		"""
		self.test_functions = []

	def register_test_function(self, wrapped_function, module_name, object_name, function_name):
		"""Add a test function to the list of registered test functions

		Args:
			wrapped_function (function): A wrapped function that takes no arguments
			module_name (String): The module name this function belongs to.
			object_name (String): The object name this function tests.
		"""
		self.test_functions.append({
			'fn': wrapped_function,
			'module_name': module_name,
			'object_name': object_name,
			'function_name': function_name
		})

	def test_all(self):
		"""Run all test functions
		"""
		self._tests_run(self.test_functions)

	def test_module(self, module_name):
		"""Test all test functions for the specified module name

		Args:
			module_name (String): The name of the module to test
		"""
		tests_to_run = []
		for tf_block in self.test_functions:
			if tf_block['module_name'] == module_name:
				tests_to_run.append(tf_block)
		
		self._tests_run(tests_to_run)

	def _tests_run(self, tf_blocks):
		"""Test the provided list of tf_blocks

		Args:
			tf_blocks (List): List of tf_blocks
		"""
		total = len(tf_blocks)
		count = 1
		successes = 0
		fails = 0
		failures = []

		for tf_block in tf_blocks:
			pct = int(100.0* count / total)
			print("\n\n\n")
			print("###########################################")
			print("#### Testing '" + tf_block['function_name'] + "'")
			print("#### Module: " + tf_block['module_name'])
			print("#### Object: " + tf_block['object_name'])
			print("#### " + str(count) + " of " + str(total) + " (" + str(pct) + "%) test functions.")
			print("###########################################")

			try:
				success = tf_block['fn']()
			except:
				traceback.print_exc()
				success = 0

			if success:
				successes += 1
				print("Test succeeded!")
			else:
				fails += 1
				failures.append(tf_block)
				print("Test failed.")

			count += 1
		
		print("\n\n\n")
		print("All tests complete. " + str(successes) + " succeeded and " + str(fails) + " failed.")
		print('\n\n')
		print("Failures:")
		for tf_block in failures:
			print(tf_block['function_name'])

test_extension = TestExtension()
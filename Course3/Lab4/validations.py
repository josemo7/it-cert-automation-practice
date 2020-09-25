#!/usr/bin/env python3

import re

def validate_user(username, minlen):
	x=True
	if type(username) != str:
		raise TypeError("username must be a string")
	if minlen < 1:
		raise ValueError("minlen must be at least 1")
	
	if len(username) < minlen:
		x=False
	# Usernames can only use letters, numbers, dots and underscores
	if re.match('^[a-z0-9._]*$', username):
		x= True
	# Usernames can't begin with a number
	if username[0].isnumeric():
		x= False

	if username[0].startswith("."):
		x= False
	if username[0].startswith("_"):
		x=False
	return x

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


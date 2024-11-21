###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter username')
password = input('Enter password')

# pattern (criteria) for username and password
username_pattern = ...
password_pattern = ...

# check if username and password are ok
username_match = re.match(username_pattern,username)
...

# print results
if ... and ...:
   print(...)
else:
   ... 
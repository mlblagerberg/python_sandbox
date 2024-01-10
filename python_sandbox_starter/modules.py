# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# import core python modules that don't need to be installed
import datetime
# from datetime import date would import just date so today could be defined as 
# today = date.today()
import time
from time import time # this imports just the time method from the time module

# import pip modules
from camelcase import CamelCase

# Import custom moduel
import validator # then use validator.validate_email or we could just import this function
from validator import validate_email


start = time() #time.time()
print(start)

# get just date
today = datetime.date.today()

# get today and time
todayTime = datetime.datetime.today()

print(today)
print(todayTime)

timestamp = time() # time.time()
print(timestamp)

totalTime = time() - start
print(totalTime)

c = CamelCase()
print(c.hump('hello there world'))

# check id email is valid
email1 = 'test%test.com'
email2 = 'test@test.com'

if validate_email(email2):
    print('Email is valid')
else:
    print('Email is not valid')

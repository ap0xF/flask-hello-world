# we are telling flask that this is the root of our project
# something like this happens when we pass __name__ to Flask class's
# constructor

"""import os
import pathlib

class Flask:
    def __init__(self, import_name):
        self.root_path = pathlib.Path(os.path.dirname(os.path.realpath(import_name)))"""

"""The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used.
Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files"""

from flask import Flask

x = Flask(__name__)

from app import routes

'''
Another peculiarity is that the routes module is imported at the bottom and not at the top of the script as it is always done.
The bottom import is a well known workaround that avoids circular imports, a common problem with Flask applications.
You are going to see that the routes module needs to import the app variable defined in this script, so putting one of the reciprocal imports at the bottom avoids the error that results from the mutual references between these two files.
'''
'''Isn't the above problem solved if I store the instance of 
Flask() to some other variable insted of naming that variable app ?????'''
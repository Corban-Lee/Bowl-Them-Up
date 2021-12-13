
#
#  Run this file to start the server.
#  To stop the server use ^C (ctrl + c) in the terminal at the /
#  bottom of your screen.
#
#  DO NOT RUN THIS FILE IN DEBUG MODE (vscode).
#  DO NOT RUN THIS FILE TWICE WITHOUT STOPPING THE SERVER.
#

from subprocess import call
call(["python", "manage.py", "runserver"])

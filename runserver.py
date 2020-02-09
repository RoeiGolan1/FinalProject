"""
This script runs the Project1RoeiGolan application using a development server.
"""

from os import environ
from Project1RoeiGolan import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

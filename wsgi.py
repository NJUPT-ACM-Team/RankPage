#!/usr/bin/python3
from rank import app as application
import sys

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8888, debug=True)

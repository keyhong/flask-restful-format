#!/bin/sh
gunicorn -w 4 -b 0.0.0.0:$FLASK_PORT app:app

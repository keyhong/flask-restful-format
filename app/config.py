"""TODO"""

import os

CONFIG_HOST = os.getenv("CONFIG_HOST", "default_host")
CONFIG_PORT = os.getenv("CONFIG_PORT", "default_port")
CONFIG_URL = os.getenv("CONFIG_HTTP_URL", "default_url")

FLASK_HOST = os.getenv("FLASK_HOST")
FLASK_PORT = os.getenv("FLASK_PORT")

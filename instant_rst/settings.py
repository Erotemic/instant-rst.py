import os

ADDITIONAL_DIRS = []

mod_dpath = os.path.dirname(os.path.abspath(__file__))

STATIC_DIR = os.path.join(mod_dpath, 'templates')
DEFAULT_FILE = os.path.join(mod_dpath, 'templates', "index.rst")
HOST = "127.0.0.1"
PORT = 5000
URL =  "http://127.0.0.1:5000"
# BROWSER = 'firefox'
BROWSER = ''
SECRET = 'JO34h#F*$HFHA@#&('

FLASK_STATIC_FOLDER = os.path.join(mod_dpath, 'static')
FLASK_TEMPLATE_FOLDER = os.path.join(mod_dpath, 'templates')


_p1 = None
_p2 = None

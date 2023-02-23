from flask import Flask  

app = Flask(__name__)

from characters import *

app.run(debug = True) 
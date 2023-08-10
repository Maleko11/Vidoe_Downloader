from flask import Flask
from auth import *

app = Flask(__name__)
app.secret_key = '12345'

app.register_blueprint(auth, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)

# https://ithelp.ithome.com.tw/m/articles/10265808

import flask
from flask import request, render_template
from flask_cors import CORS
import app

flaskApp = flask.Flask(__name__, static_url_path="/static/", static_folder='app/static/', template_folder='app/templates/')
CORS(flaskApp)

app.runApp(flaskApp) # 比較複雜的用法

@flaskApp.route("/")
def baseTester():
  return render_template("index.html")

if __name__ == '__main__':
  flaskApp.run(host="127.0.0.1", port=5566, debug=True)
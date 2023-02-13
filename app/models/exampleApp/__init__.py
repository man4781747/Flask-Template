#https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.add_url_rule
from . import route

def runApp(flask_app):
  flask_app.add_url_rule("/api/Test", view_func=route.apiTest)

  @flask_app.route("/api/Test2")
  def test2():
    return "abc"

  return flask_app


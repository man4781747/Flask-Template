from .models import exampleApp

def runApp(flask_app):
  exampleApp.runApp(flask_app)
  
  return flask_app
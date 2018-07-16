from flask import Flask
app = Flask(__name__)
@app.route("/")
def index(name= "student"):
  return "welcome {} to Akirachix".format(name)

@app.route("/welcome/<name>")
def welcome(name= "student"):
  return "welcome {} to Akirachix".format(name)
  
if __name__ == '__main__':
  app.run(host = '0.0.0.0',port=8080)
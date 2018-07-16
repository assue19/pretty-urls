
from flask import Flask
from circle import Circle
app = Flask(__name__)
@app.route("/")
def index(name= "student"):
  return "welcome {} to Akirachix".format(name)
@app.route("/circle/<int:radius>")
@app.route("/circle/<float:radius>")
def circle(radius = 0):
  circ =  Circle(radius)
  return "Area of circle is {}".format(circ.area())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
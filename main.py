from flask  import Flask
from square import Square
from circle import Circle
from rectangle import Rectangle
app = Flask(__name__)
@app.route("/")
def index(name = "student"):
  return "welcome {} to Akirachix".format(name)

@app.route("/welcome/<name>")
def welcome(name = "student"):
   return "Welcome {} to Akirachix".format(name)
@app.route("/square/<int:length>") 
@app.route("/square/<float:length>") 
 
def square(length= 0):
  sqr = Square(length)
  return "Area of square  is {}".format(sqr.area())

  #end of square

@app.route("/rectangle/<int:length>/<int:width>") 
@app.route("/rectangle/<float:length>/<float:width>") 
@app.route("/rectangle/<float:length>/<int:width>")  
@app.route("/rectangle/<int:length>/<float:width>") 
def rectangle(length= 0,width= 0):
  rect = Rectangle(length,width)
  return "Area of rectangle  is {}".format(rect.area())
   #end od rectangle

@app.route("/circle/<int:radius>")
@app.route("/circle/<float:radius>")
def circle(radius = 0):
  circ =  Circle(radius)
  return "Area of circle is {}".format(circ.area())

if __name__ == '__main__':
   app.run(host = "0.0.0.0",port=8080)
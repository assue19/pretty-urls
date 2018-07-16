from flask  import Flask
from square import Square
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

if __name__ == '__main__':
   app.run(host = "0.0.0.0",port=8080)
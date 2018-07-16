from flask  import Flask
from rectangle import Rectangle
app = Flask(__name__)
@app.route("/")
def index(name = "student"):
  return "welcome {} to Akirachix".format(name)

@app.route("/welcome/<name>")
def welcome(name = "student"):
   return "Welcome {} to Akirachix".format(name)
@app.route("/rectangle/<int:length>/<int:width>") 
@app.route("/rectangle/<float:length>/<float:width>") 
@app.route("/rectangle/<float:length>/<int:width>")  
@app.route("/rectangle/<int:length>/<float:width>") 
def rectangle(length= 0,width= 0):
  rect = Rectangle(length,width)
  return "Area of rectangle  is {}".format(rect.area())

if __name__ == '__main__':
   app.run(host = "0.0.0.0",port=8080)
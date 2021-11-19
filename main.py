#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
pear_image = "pear.gif" # Store the file name of your shape
apple_image = "apple.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file
wn.addshape(apple_image)
pear = trtl.Turtle()
apple = trtl.Turtle()
pear2 = trtl.Turtle()
pear3 = trtl.Turtle()
pear4 = trtl.Turtle()

pear2.hideturtle()
pear2.penup()
pear2.shape(pear_image)
pear2.goto(-90,120)
pear2.showturtle()
pear2.speed(1)

pear3.hideturtle()
pear3.penup()
pear3.shape(pear_image)
pear3.goto(40,100)
pear3.showturtle()
pear3.speed(1)

pear4.hideturtle()
pear4.penup()
pear4.shape(pear_image)
pear4.goto(100,60)
pear4.showturtle()
pear4.speed(1)

apple.hideturtle()
apple.penup()
apple.shape(pear_image)
apple.goto(-100,60)
apple.showturtle()

pear.speed(1)
apple.speed(1)
pear.right(90)
#-----functions-----

def pear2_fall():
  pear2.penup()
  pear2.clear()
  pear2.goto(-90,-150)
  pear2.hideturtle()
def draw_a_C():
  pear2.penup()
  pear2.goto(-90,120)
  pear2.color("black")
  pear2.write("C", font=("Arial", 20, "bold"))
  pear2.goto(-80,125)

def pear3_fall():
  pear3.penup()
  pear3.clear()
  pear3.goto(40,-150)
  pear3.hideturtle()
def draw_a_D():
  pear3.penup()
  pear3.goto(40,120)
  pear3.color("black")
  pear3.write("D", font=("Arial", 20, "bold"))
  pear3.goto(45,120)

def pear4_fall():
  pear4.penup()
  pear4.clear()
  pear4.goto(100,-150)
  pear4.hideturtle()
def draw_an_E():
  pear4.penup()
  pear4.goto(100,60)
  pear4.color("black")
  pear4.write("E", font=("Arial", 20, "bold"))
  pear4.goto(100,70)

def apple_fall():
  apple.penup()
  apple.clear()
  apple.goto(-90,-150)
  apple.hideturtle()
def draw_a_B():
  apple.penup()
  apple.goto(-105,55)
  apple.color("black")
  apple.write("B", font=("Arial", 20, "bold"))
  apple.goto(-90,60)
def pear_fall():
  pear.penup()
  pear.clear()
  pear.goto(0, -150)
  pear.hideturtle()
def draw_an_A():
  pear.penup()
  pear.goto(-10,-10)
  pear.color("black")
  pear.write("A", font=("Arial", 20, "bold")) 
  pear.goto(0,0)
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

draw_pear(pear)
draw_an_A()
draw_a_B()
draw_a_C()
draw_a_D()
draw_an_E()
#-----function calls-----

wn.bgpic("background.gif")
wn.listen()
wn.onkeypress(apple_fall, "b")
wn.onkeypress(pear_fall, "a")
wn.onkeypress(pear2_fall, "c")
wn.onkeypress(pear3_fall, "d")
wn.onkeypress(pear4_fall, "e")
wn.mainloop()

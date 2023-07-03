# cookie clicker
import turtle
#make the screen, tell it what to make the title bar say, tell it the Background (BG) color
wn = turtle.Screen()
wn.title("ok hi guys")
wn.bgcolor("black")
#tell it the shape
wn.register_shape("cookie.gif")
#make the cookie into a turtle, make the shape the image you want it to be, and set the animation speed (in this case, 0, b/c its an image)
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)
#make our variable 'clicks' for how many time the user clicked it
clicks = 0
#turn our variable into a turtle so it can be displayed, hide it, make the color white (it is text), make it go to a certain area, and then make it write in that font and size and type that message aligned.
pen =  turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
#basically make what happens when it is clicked below. to add one click to our variable above, and hten change the text to account for it)
def clicked(x, y):
    global clicks 
    clicks += 1
    pen.clear() 
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
#when cookie is clicked it will add one click and change the text and do the def clicked thing
cookie.onclick(clicked)
#thats mainloop
wn.mainloop()
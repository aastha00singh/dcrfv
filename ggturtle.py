import turtle 
screen = turtle.Screen() 
screen.title("Concentric Circles") 
screen.bgcolor("white") 
pen = turtle.Turtle() 
pen.speed(10) 
 

def draw_concentric_circles (num_circles):

    radius = 10 
    for _ in range(num_circles): 
        pen.circle(radius) 
        radius += 10           
pen.penup() 
pen.goto(0, 0) 
pen.pendown() 
draw_concentric_circles(10)  
screen.exitonclick() 
import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple',  'blue',  'green',  'orange', 'yellow']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
  for x in range(200):
      t.pencolor('green')
      t.width(x/100 +1)
      t.forward(x)
      t.left(79)
  t.right(239)
  for x in range(200, 0, -1):
        t.pencolor('red')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)
      

from Functions import*
turtle.bgcolor(0,0,0)
bob.speed(0)
bob.width(5)

for times in range(254):
    polygon(3,300-times,(0,255-times,255-times))
    bob.right(25)
    bob.fd(10)


jump(-870,350)
bob.left(230)

for times in range(35):
    bob.color(255,255,0)
    bob.circle(75)
    bob.fd(50)

bob.right(90)
bob.color(255,0,0)

for times in range(15):
    bob.circle(75)
    bob.fd(50)

bob.right(90)
bob.color(255,0,255)

for times in range(35):
    bob.circle(75)
    bob.fd(50)
bob.right(90)
bob.color(182,91,153)

for times in range(15):
    bob.circle(75)
    bob.fd(50)

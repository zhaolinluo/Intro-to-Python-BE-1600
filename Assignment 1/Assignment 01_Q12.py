#Write a function that draws a series of 10 squares, with each square being 
# 10 pixels smaller on each side. 


import turtle


tur = turtle.Turtle()


def main(tur,sl):
    
    for a in range (4):
        
        tur.forward(sl)
        
        tur.left(90)
        
    tur.up()
    
    tur.forward(5)
    
    tur.left(90)
    
    tur.forward(5)
    
    tur.right(90)
    
    tur.down()

#going down each time by 10 pixels
main(tur,200)

main(tur,190)

main(tur,180)

main(tur,170)

main(tur,160)

main(tur,150)

main(tur,140)

main(tur,130)

main(tur,120)

main(tur,110)




main=turtle.Screen()

main.setup(startx=0,starty=0)


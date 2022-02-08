
#Miles = Kilometers * 0.6214
#The program should use a function that accepts kilometers as an argument and prints 
#the equivalent miles.


def main(km):
    #conversion equ.
    miles = km * 0.6214
    #last statement 
    print("The conversion of ", km , "kilometers \nto miles is ", miles,"miles.")

#user input 
miles = float(input("Enter the distance in kilometers: "))
main(miles)

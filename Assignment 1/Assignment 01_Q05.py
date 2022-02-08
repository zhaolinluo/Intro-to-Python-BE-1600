# There are three seating categories at a stadium.
# A seats = $15, Class B seats = $12 Class C = $9.

one = int(input("Enter count of A seats: "))
two = int(input("Enter count of A seats: "))
three = int(input("Enter count of A seats: "))

def func1(one):
    x = (one*15)
    print("Income from class A seats: $ ",x, end = " ",)


def func2(two):
    y = (two*12)
    print("\nIncome from class B seats: $ ",y, end = " ",)



def func3(three):
    z = (three*9)
    print("\nIncome from class C seats: $ ",z, end = " ",)

def func4(one, two, three):
    a = (one*15)+(two*12)+(three*9)
    print("\nTotal Income: $ ",a, end = " ")


func1(one)
func2(two)
func3(three)
func4(one,two,three)
    

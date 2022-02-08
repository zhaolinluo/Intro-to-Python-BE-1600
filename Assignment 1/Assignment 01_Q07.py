# 515 square feet of wall = one gallon of paint = eight hours labor
# $20.00 per hour for labor
# display
# the number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job


import math
#user input

WallSpace = float(input("Enter wall space in square feet: "))

Cost = float(input("Enter paint price per gallon: "))

def main():
    
    numofGal = math.ceil(float(WallSpace/115))
    
    WorkHr = math.ceil(float(numofGal *8))
    
    CostPaint = float(numofGal*Cost)
    
    CostWork = (WorkHr*20)
    
    SumCost = float(CostPaint+ CostWork)

#print the variables 
    print("Gallons of Paint: ", numofGal, "\nHours of labor: ", WorkHr, "\nPaint Charges: $", CostPaint, "\nLabor Charges: $", CostWork, "\nTotal Hours: $ ", SumCost)

main()

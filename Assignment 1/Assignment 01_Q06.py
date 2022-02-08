#state sales tax rate is 4 percent
#county sales tax rate is 2 percent
#asks the user to enter the total sales for the month.
#display:
#The amount of monthly sales
#The amount of state sales tax
#The amount of county sales tax
#The total sales tax (county plus state)

#user input
MonthSales = float(input("Enter the total sales for the month: "))

def sum(month):
    #equa. for each tax rate
    state = float(month*0.04)
    county = float(month*0.02)
    total = float(county+state)

    #printing out results
    print("Monthly sales: $", month, "\nState tax: $", state, "\nCounty tax: $", county, "\nTotal tax: $",total)

sum(MonthSales)

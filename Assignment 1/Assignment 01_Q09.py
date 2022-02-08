#loop should iterate 10 times and keep a running total of the numbers entered.

NUM = 0
for a in range(10):
    NUM += float(input("Enter a number: "))

print("The total is" , NUM)

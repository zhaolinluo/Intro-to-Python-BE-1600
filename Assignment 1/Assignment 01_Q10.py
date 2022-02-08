#Running on a particular treadmill you burn 3.9 calories per minute. Write a 
#program that uses a for loop to display the number of calories burned after 10, 15, 20, 
#25, and 30 minutes.

print("Minutes\tCalories Burned", "\n------------------------")
def main():
    for a in range(10,31,5):
        print(a,"\t",a*3.9)
main()

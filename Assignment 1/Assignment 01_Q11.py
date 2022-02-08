#Write a function that takes two integers, A and B; the function prints all 
#numbers in the range A to B (inclusive) and return their sum.


A = 5
B = 10

def main1(A,B):
    for i in range(A,B+1):
        print(i, end = " ")
    SUM = 0
    for i in range(A,B+1):
        SUM += i
        
    SUM=list(range(A,B))
#returning the sum
    print("\nsum of numbers:",(sum(range(A, B+1))))


main1(A,B)


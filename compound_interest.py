# Coding Challenge 1, compound_interest.py
# Name: Prasiddha Regmi
# Student No: 210178

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!
print("                      *COMPOUND INTEREST*                      ")
print("                           Well-Come!                          ")
print("The program to find the compound interest easily by giving the data from user.")
print("                                                 Created by : Prasiddha Regmi")
p = float(input("What is the principle amount?"))
initial = p
r = float(input("What is the rate?"))
t = int(input("What is the number of years?"))
n = int(input("What is the number of times the interest is compounded per year?"))
count=int(1)
print("Year\tPeriod\tOld Balance\tInterest\tNew Balance")
print("-"*59)

for x in range(t):
    print(x+1,end="\t")
    for y in range(n):
        print(count,end="\t")
        print("£",round(p,2),end="\t")
        i = (p*(1/n)*r)/100
        print("£",round(i,2),end="\t\t")
        new = p+i
        print("£",round(new,2))
        p= new
        if(y<(n-1)):
            print("",end="\t")
        count=count+1
print("£",initial,"invested at",r,"% for",t,"years compounded",n, "times per year is: £",round(new,2))


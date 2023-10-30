num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
div = num1/num2
print("The division with only two decimal is %0.2f" %div)
print("The division with scientific notation is %0.2e" %div)
print("The division with scientific notation is {:0.2e}".format(div))

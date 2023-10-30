def display(num1, num2):
    ret = (num1 / num2)
    return ret;
n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
result = display(n1, n2)
print('The average of number= %0.2f'%result)

num = float(input("Enter the number : "))

if (num % 5 == 0) and (num % 3 == 0):
    print("FizzBizz")
elif (num%5 == 0):
    print("Buzz")
elif (num%3 == 0):
    print("Fizz")
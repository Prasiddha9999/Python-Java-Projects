sum=0
while True:
    user_input=str(input("Enter a number or type stop : "))
    if (user_input)=='stop':
        break
    else:
        sum+=int(user_input)
print("You stopped the loop and the sum is :",sum)

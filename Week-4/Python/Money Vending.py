user_money=int(input("Enter the sum of money : "))

if user_money>0:
    print("\nChange\t50p\t20p\t10p\t5p\t2p\t1p\n")
    print("--"*len("\nChange\t50p\t20p\t10p\t5p\t2p\t1p\n"))
    print(user_money,end="\t")
    money=0
    print(user_money//50,end="\t")
    money=user_money-50*(user_money//50)
    print(money//20,end="\t")
    money=money-20*(money//20)
    print(money//10,end="\t")
    money=money-10*(money//10)
    print(money//5,end="\t")
    money=money-5*(money//5)
    print(money//2,end="\t")
    money=money-2*(money//2)
    print(money//1)
    print("\nThe returning change of {0} are above ".format(user_money))
else:
    print("\nUser input is negative")


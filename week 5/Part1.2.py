list=[]
for x in range(10):
    a=int(input("enter number:"))
    if (a<100 and a>1):
        list.append(a)
    else:
        list.append("over")
print(list)

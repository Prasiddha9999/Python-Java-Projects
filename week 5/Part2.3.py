d={}
def get_daily_temp(x,y):
    d.update({x:y})
    return d
z ="y"
while z=="y":
    day = input ("What day is today?")
    temp = input ("What is the  avg temperature for today?")
    z= input("Do you want to give another average daily temp?()Y/N")
    D = get_daily_temp(day,temp)
print(D)


d={}
def add_daily_temp(day, temp):
    if day not in d:
        d.update({day:temp})
    return d
x = input ("What is the temperature for today?")
y = input ("What day is today?")
print(add_daily_temp(y, x))

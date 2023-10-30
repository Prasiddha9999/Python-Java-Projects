list=[]
def moderate_days(x):
    for y in x.values():
        if y>70 and y<79:
            list.append(y)
    return list
dict = {"s":60, "m":77, "t":88, "w":78, "th":32, "fr":22, "sat":88}
print(moderate_days(dict))


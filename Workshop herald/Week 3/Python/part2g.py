def either_side(value):
    return value;
n1 = int(input("Enter value"))
val = either_side(n1)
less = val-1
more = val+1
print("You typed", val,", one less than",val,"is",less,", one more than",val,"is",more)

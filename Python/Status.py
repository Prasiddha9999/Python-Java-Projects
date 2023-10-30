point = float(input("Enter the no of point earned : "))

if point >= 90:
    print("Senior Status")
elif point >= 60:
    print("Junior Status")
elif point >= 30:
    print("Sophomore Status")
else:
    print("Freshman Status")
seconds  = int(input("Enter the time"))

second = int (seconds % 60)
hour = int (seconds / 60)
minute = int (hour % 60)

hour = int (hour / 60)

print("Hour:Min:Sec - ", hour , ":" , minute , ":" , second)
      
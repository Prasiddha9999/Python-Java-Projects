def print_multiline_heading(name, years):
    return (name, years)
yrs = int(input("Enter years"))
nam = str(input("Enter name"))
val = print_multiline_heading(nam, yrs)

print("Dear Feline Fanatic,\nYour cat has been arrested for:\n\t1.Catnapping\n\t2.Cat burglary\n\t3.Extortion.\nIt will be sentenced to",yrs ,"in prison.\nSincerly,", nam)

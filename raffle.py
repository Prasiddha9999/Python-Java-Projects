#A

def validate_name(name):
    count=0
    for i in name:
        if(i.isspace()):
            count=count+1
    if(count==0 or count>1):
        return False
    else:
        names = name.split()
        if(len(names)!=2):
            return False
        else:
            for j in names:
                if(not j.isalpha()):
                    return False
    return True




import random

entrants = list()

while True:
    while (True):
        temp = input('Enter participant name\n> ')
        if(not temp):
            break
        else:
            if(validate_name(temp)):
                name = temp
                break
            else:
                print("Name not Valid! Enter Again")
        
    if not temp:
        break
    phone = input('Enter participant contact number\n> ')
    entrants.append([name, phone])

print('Competition Finished!')
winner = random.choice(entrants)
print('The winner is: {0}, contact number is:{1}'.format(winner[0],winner[1]))



#B
def validate_name(name):
    count=0
    for i in name:
        if(i.isspace()):
            count=count+1
    if(count==0 or count>1):
        return False
    else:
        names = name.split()
        if(len(names)!=2):
            return False
        else:
            for j in names:
                if(not j.isalpha()):
                    return False
    return True


def validate_contact(c):
    if(not c.isdecimal()):
        return False
    if(len(c)!=10 and len(c)!=11):
        return False
    return True


import random

entrants = list()

while True:
    while (True):
        temp = input('Enter participant name\n> ')
        if(not temp):
            break
        else:
            if (validate_name(temp)):
                name = temp
                break
            else:
                print("Name not Valid! Enter Again")
        
    if not temp:
        break
    while (True):
        temp = input('Enter participant contact number\n> ')
        if(validate_contact(temp)):
            phone = temp
            break
        else:
            print("Contact number not valid! Enter Again")
    entrants.append([name, phone])

print('Competition Finished!')
winner = random.choice(entrants)
print('The winner is: {0}, contact number is:{1}'.format(winner[0],winner[1]))




#C


def validate_name(name):
    count=0
    for i in name:
        if(i.isspace()):
            count=count+1
    if(count==0 or count>1):
        return False
    else:
        names = name.split()
        if(len(names)!=2):
            return False
        else:
            for j in names:
                if(not j.isalpha()):
                    return False
    return True


def validate_contact(c):
    if(not c.isdecimal()):
        return False
    if(len(c)!=10 and len(c)!=11):
        return False
    return True

def validate_email(e):
    if(e.endswith('@hotmail.co.uk') or e.endswith('@gmail.co.uk')):
        return True
    return False


import random

entrants = list()

while True:
    while (True):
        temp = input('Enter participant name\n> ')
        if(not temp):
            break
        else:
            if(validate_name(temp)):
                name = temp
                break
            else:
                print("Name not Valid! Enter Again")
        
    if not temp:
        break
    while (True):
        temp = input('Enter participant contact number\n> ')
        if(validate_contact(temp)):
            phone = temp
            break
        else:
            print("Contact number not valid! Enter Again")

    while (True):
        temp = input('Enter participant email address\n> ')
        if(validate_email(temp)):
            email = temp
            break
        else:
            print("Email not valid! Enter Again")

    entrants.append([name, phone, email])

print('Competition Finished!')
winner = random.choice(entrants)
print('The winner is: {0}, contact number is:{1}, email is:{2}'.format(winner[0],winner[1],winner[2]))


#D
def validate_name(name):
    count=0
    for i in name:
        if(i.isspace()):
            count=count+1
    if(count==0 or count>1):
        return False
    else:
        names = name.split()
        if(len(names)!=2):
            return False
        else:
            for j in names:
                if(not j.isalpha()):
                    return False
    return True


def validate_contact(c):
    if(not c.isdecimal()):
        return False
    if(len(c)!=10 and len(c)!=11):
        return False
    return True

def validate_email(e):
    if(e.endswith('@hotmail.co.uk') or e.endswith('@gmail.co.uk')):
        return True
    return False


import random

entrants = list()

print("Welcome to the raffle! What would you like to do?\n")
while True:
    choice=input('1. Add Entrants\t\t2.Remove Entrants\t3.View Entrants\t\t4.Continue\n')
    if(choice == '4'):      
        break
    if(choice=='3'):
        print(entrants)
    if(choice=='2'):
        print("Enter the details of the entrants you want to remove")
        rname = input("Name")
        rcontact = input("Contact number")
        remail = input("Emal")
        entrants.remove([rname,rcontact,remail])
    if(choice == '1'):
        while True:
            while (True):
                temp = input('Enter participant name\n> ')
                if(not temp):
                    break
                else:
                    if(validate_name(temp)):
                        name = temp
                        break
                    else:
                        print("Name not Valid! Enter Again")
                
            if not temp:
                break
            while (True):
                temp = input('Enter participant contact number\n> ')
                if(validate_contact(temp)):
                    phone = temp
                    break
                else:
                    print("Contact number not valid! Enter Again")

            while (True):
                temp = input('Enter participant email address\n> ')
                if(validate_email(temp)):
                    email = temp
                    break
                else:
                    print("Email not valid! Enter Again")

            entrants.append([name, phone, email])




print('Competition Finished!')
winner = random.choice(entrants)
print('The winner is: {0}, contact number is:{1}, email is:{2}'.format(winner[0],winner[1],winner[2]))




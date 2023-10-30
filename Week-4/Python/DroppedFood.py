
print("You Dropped your Food ")
ans = (input("Did any one see you (Yes or No) "))
if ans == "yes":
    ans=input("Was it your boss/love/parent ")
    if ans =="yes":
        ans=input("Was it expensive (Yes or No) ")
        if ans =="yes":
            ans=input("Can you cutt of the part that touched the floor ? (Yes or No) ")
            if ans =="yes":
                print("Eat it ")
            else:
                print("Your call")
        else:
            ans=input("Is it bacon ? (Yes or No)")
            if ans =="yes":
                print("Eat it ")
            else:
                print("Dont Eat ")
    else:
        print("Eat it :)")
else:
        ans = input("Was it Sticky ? Yes or No ")
        if ans == "yes":
            ans = input ("Is it a raw Steak (Yes / No) ")
            if ans == "yes":
                ans = input("Are you a puma ? (Yes or No) ")
                if ans=="yes":
                    print("Eat it ")
                else:
                    print("Dont eat ")
            else:
                def cat():
                    ans = input ("Did your cat lick it (Yes or No) ")
                    if ans=="yes":
                        ans = input ("Is your cat healthy (Yes or No) ")
                        if ans =="yes":
                            print("Eat it ")
                        else:
                            print ("Dont eat ")
                    else:
                        print("Eat it ")
        else:
            ans= input("Is it an Emausaurus (Yes / No) ")
            if ans =="yes":
                ans = input ("Are you Megalosaurus ? (Yes or No) ")
                if ans =="yes":
                    print("Eat it ")
                else:
                    print("Dont eat ")
            else:
                cat()
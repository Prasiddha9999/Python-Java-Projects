print('start')
print('helo')
print('openning the file')
try:
    a= int(input("enter"))
    b= int(input("enter"))
    fp=open('file.txt', 'r')
    print('file oppened')
    print(a/b)
except IOError:
    print('IOError')
except ZeroDivisionError:
    print("ZerodivisionError")
except ValueError:
    print("Value Error")
except:
    print("Not known")

print('end')

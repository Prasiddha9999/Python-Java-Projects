fp=open('file3.txt', 'r')
l = 1
for line in fp:
    l +=   1
    if l%2 != 0:
       
        print(line)



fr=open('file3.txt', 'r')
count=0
for line in fr:
    for txt in line:
        if txt=='e':
            count+=1
print(count)
fr.close()



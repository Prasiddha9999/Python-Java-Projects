def extra_temp(line):
    for ch in line:
        if ch.isdigit():
            print(ch,end='')

fp= open('file.txt', 'r')
line= fp.readline()
extra_temp(line)
    

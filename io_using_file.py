poem = '''\
    programming is fun
    when the work is done
    if you wanna make your work also fun:
        use python'''

# open file for editing ('w')
f = open('poem.txt', 'w')
# write text into the file
f.write(poem)
# close file
f.close()

# if not specified, file will be open with 'r' mode
f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
        
    print(line, end='')

f.close()

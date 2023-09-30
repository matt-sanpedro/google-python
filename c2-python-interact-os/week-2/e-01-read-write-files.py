# with block will automatically close the file
with open('spider.txt') as file:
    # print(file.readline())
    for line in file:
        print(line.strip().upper())

# open the file
file = open('spider.txt')
# read all the lines
# warning: if file is large, this can take a lot of computer memory
lines = file.readlines()
# close the file
file.close()

lines.sort()
print(lines)

# writing to file
# by default, the open function uses the "r" mode for "read only"
"""
MODES
r: read only
w: write only [will delete content if it exists]
a: append to end fo file
r+: read-write
"""
with open('novel.txt', 'w') as file:
    file.write('Hold fast to your dreams')

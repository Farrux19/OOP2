import os ; os.system("cls")

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
dc = {}
c = 0 ; z = 0 ; x = 0; v = 0 ; b = 0

for i in myList:
    if i == 1:
        c += 1
    elif i == 2:
        z += 1
    elif i == 3:
        x += 1
    elif i == 4:
        v += 1
    elif i == 5:
        b += 1
dc[1] = c
dc[2] = z
dc[3] = x
dc[4] = v
dc[5] = b

print(dc)
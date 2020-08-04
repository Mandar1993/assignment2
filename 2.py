rows = 5
for num in range(rows):
    for i in range(num):
        print("*", end=" ")  # print number
     #line after each row to display pattern correctly
    print(" ")
rowss = 5
b = 0
for i in range(rowss, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\r')

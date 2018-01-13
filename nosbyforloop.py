arr = [ ]
n = int(input("Enter the number : "))
for i in range(n):
    x = input()
    arr.append(x)

file = open("nosbyforloop.txt",'w')
for i in arr:
    file.write(str(i)+"\n")

file.close()

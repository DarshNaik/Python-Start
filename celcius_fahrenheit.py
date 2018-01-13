def c_f(x):
    if x <-273.15:
        return "This temperaure is impossible unless you are an alien"
    else:
        f = x * 1.8 + 32.0
        return f

c = []
n = int(input("Enter a number : "))
for i in range(n):
    x = float(input())
    c.append(x)

for i in c:
    print(c_f(i))

def c_f(x):
    if x <-273.15:
        return "This temperaure is impossible unless you are an alien"
    else:
        f = x * 1.8 + 32.0
        return f

a = []
n = int(input("Enter a number : "))
for i in range(n):
    x = float(input())
    a.append(x)

for i in a:
    print(c_f(i))

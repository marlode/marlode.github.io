global x
global y
x = 2
y = 2


def h (i):
    x =+ 1
    return 4


e = (h(y) + x) * y
print(y)
print(x)
print(e)

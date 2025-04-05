def c_to_f(f):
    c = 5*(f-32)/9
    return c

f =int(input ("Enter temperature in f:"))
c = (c_to_f(f))
print(f"{round(c, 2)}")
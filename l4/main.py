def calc2(a,b):
    return a*b

calc1 = lambda a,b: a+b

def math(op,x,y):
    print(op(x,y))


math(calc1,5,4)

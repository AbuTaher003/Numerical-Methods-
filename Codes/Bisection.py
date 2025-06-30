import math

def f(x):
    return 3*x - math.cos(x) - 1

def Bisection(a,b,iteration):
    if f(a) * f(b) >= 0:
        print("Invalid a and b")
        return None
        
    print("initial interval : a =",a , "and b =",b)

    for step in range (1, iteration+1):
        c = (a+b)/2
        print(f"step-{step:.6f} c={c:.6f} f(c)={f(c):.6f}")

        if f(c) == 0:
            break
        elif f(a) * f(c) > 0:
            a = c
        else:
            b = c

    return c

iteration = 8
root = Bisection(a = 0, b = 1, iteration = iteration)
print(f"After {iteration} iterations the root is : {root}")

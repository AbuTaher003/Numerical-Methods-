import math

def f(x):
    return 3*x - math.cos(x) - 1

def Regula_falsi(a, b, iteration):
    if f(a) * f(b) >= 0:
        print("Invalid interval.")
        return None
    
    print("initial interval : a =",a , "and b =",b)

    for i in range(1, iteration+1):
        c = (a*f(b)-b*f(a))/(f(b) - f(a))

        print(f"step-{i}: a={a:.6f} b={b:.6f} c={c:.6f} f(c)={f(c):.6f}")

        if f(c) == 0:
            break
        elif f(a) * f(c) > 0:
            a = c
        else: 
            b = c
    return c
        

root = Regula_falsi(a=0,b=1, iteration= 10)
print("the root is: ",root)

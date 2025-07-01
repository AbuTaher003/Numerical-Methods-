import math

def f(x):
    return 3*x - math.cos(x) -1

def df(x):
    return 3 + math.sin(x)

def Newton_Raphson(x0, iteration):
    print("Initial Guess x0 = ",x0,"\n")

    for i in range(1,iteration+1):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Zero derivation, method fails.")
            return None

        x1 = x0 - fx/dfx

        print(f"step-{i} : x = {x1:.6f}, f(x) = {f(x1):.6f}")

        x0 = x1

    return x1

root = Newton_Raphson(x0=0, iteration=5)
print(f"\nAfter 5 iterations the root is :",root)

import math

def g(x):
    return (math.cos(x)+1)/3

def fixed_point(x0, iteration):
    print("Initial guess: ",x0,"\n")

    for i in range (1,iteration+1):
        x1 = g(x0)

        print(f"step-{i}: x ={x1:.6f}")

        x0 = x1

    return x1

root = fixed_point(x0=3.2, iteration=10)
print("\nThe root is : ",root)
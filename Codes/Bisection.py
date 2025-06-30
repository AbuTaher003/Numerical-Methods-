import math
def f(x):
    return 3*x - math.cos(x) - 1   # এখানে নিজের function বসাও

def bisection(a, b, iterations):
    if f(a) * f(b) >= 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
        return None

    print("initial interval : a =",a , "and b =",b)

    for step in range(1, iterations + 1):
        c = (a + b) / 2
        print(f"Step {step}: c = {c:.6f}, f(c) = {f(c):.6f}")

        if f(c) == 0:
            # exact root found
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c


# Example usage
iterations = 8
root = bisection(a=0, b=1, iterations=iterations)
print(f"\nEstimated root after {iterations} iterations: {root}")

def gauss_elimination(a, b):
    n = len(b)

    # Forward Elimination
    for i in range(n):
        # Make the diagonal element 1 and eliminate below
        for j in range(i+1, n):
            if a[i][i] == 0:
                print("Division by zero error!")
                return None
            ratio = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] = a[j][k] - ratio * a[i][k]
            b[j] = b[j] - ratio * b[i]

    # Back Substitution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i][i]

    return x


# Example usage
a = [[1, 1, 1],
     [2, -3, 4],
     [3, 4, 5]]

b = [9, 13, 40]

solution = gauss_elimination(a, b)

print("\nSolution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.4f}")

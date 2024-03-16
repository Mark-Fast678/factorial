def factorial_r(n):
    if n == 1 or n == 2:
        return n

    return (n *  factorial_r(n - 1))

res = factorial_r(1000)
print(res)
#should be non-recurcive
def factorial(n):
    if n == 1 or n == 2:
        return n

    f = n
    for i in range(1, n):
        f = f * i

    return f

res = factorial(1550)
print(res)
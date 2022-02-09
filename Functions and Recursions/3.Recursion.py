# factorial using for loop
# basic  : 1 * 2 * 3 * 4 * ... * n
# sorted : [1 * 2 * 3 * 4 * ... n-1] * n
# revised new formula : (n-1) * n

# Recursion : Function call itself
# in this method we are not use recursion method
def factorial_iterative(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


print(factorial_iterative(5))


# here we use recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    # below line show function call itself
    return n * factorial_iterative(n - 1)


print(factorial_recursive(5))

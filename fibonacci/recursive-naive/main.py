# Naive implementation of recursive Fibonacci

# Fibonacci sequence is defined as a sequence starting with 0 and 1 and the following numbers
#   are the sum of the two previous numbers.

# We can generalize as: fib(n) = fib(n - 1) + fib(n - 2)

def fib(n: int) -> int:
    """
    Calculates the n number of fibonacci sequence

    Args:
        n: an integer value of nth number to be calculated.

    Returns:
        The nth number of fibonacci sequence
    """
    if n < 2: return n

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib(20))
    print(fib(50)) # it takes forever to calculate because of multiple recursive calls

# Iterative implementation of Fibonacci

def fib(n: int) -> int:
    """
    Calculates the n number of fibonacci sequence

    Args:
        n: an integer value of nth number to be calculated.

    Returns:
        The nth number of fibonacci sequence
    """
    if n == 0: return n

    prev: int = 0
    next: int = 1

    for _ in range(1, n):
        prev, next = next, prev + next

    return next


if __name__ == "__main__":
    print(fib(10))
    print(fib(50))
    print(fib(120))

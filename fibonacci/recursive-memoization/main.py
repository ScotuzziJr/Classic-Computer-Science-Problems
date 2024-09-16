# Recursive implementation of Fibonacci using memoization

from typing import Dict

# the first two numbers will always be 0 and 1 so we can initialize the memo dict with them
memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    """
    Calculates the n number of fibonacci sequence

    Args:
        n: an integer value of nth number to be calculated.

    Returns:
        The nth number of fibonacci sequence
    """
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2) # memoization

    return memo[n]

if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib(20))
    print(fib(50))
    print(fib(120))

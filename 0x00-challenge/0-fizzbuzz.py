#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz prints the list at the end of function and collect items into a list

    """
    if n < 1:
        return

    tmp_ret = []
    for i in range(1, n + 1):
        if (i % 3) == 0:
            tmp_ret.append("Fizz")
        elif (i % 3) == 0 and (i % 5) == 0:
            tmp_ret.append("FizzBuzz")
        elif (i % 5) == 0:
            tmp_ret.append("Buzz")
        else:
            tmp_ret.append(str(i))
    print(" ".join(tmp_ret))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing count")
        print("Usage: ./0-fizzbuzz.py <count>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    count = int(sys.argv[1])
    fizzbuzz(count)

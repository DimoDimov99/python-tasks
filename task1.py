def factorial(number: int) -> int:
    """Simple function to calculate and return factorial of given n number"""
    result = 1
    if number == 0:  # handle 0 as corner case
        return 1
    elif number < 0:  # absolute value, math.abs() can be used as well
        number *= -1
    for i in range(1, number + 1):
        result *= i
    return result


def factorial_rec(number: int) -> int:
    # This and fibonacci is the max of my ability to use recursion :D
    """Simple recursion function to calculate and return factorial of given n number"""
    if number < 0:
        number *= -1
    return number * factorial_rec(number - 1) if number > 0 else 1


if __name__ == "__main__":
    print(factorial(5))
    print(factorial_rec(6))

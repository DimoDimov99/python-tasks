def greeting(first_name: str, last_name: str, sum_of_money: float) -> str:
    """Docstring"""
    # user input is accepted with input function, everything that it takes is casted to string,
    # so to get float we need to type cast float(input())
    return f"Hello {first_name} {last_name}, you have ${sum_of_money} in your account."


if __name__ == "__main__":
    print(greeting("John", "Doe", 523.78))

import math


def calculate_area(shape: str, radius=1, length=1, width=1): # In cases like this, you don't want default values, as if someone forgets to add an argument, the function will return a static value, making it hard to pinpoint if there is an issue. A proper `sentinel` value might be None, as it can safely be checked.
    if shape.lower() == "circle":
        return round(math.pi * (radius * radius), 2)
    elif shape.lower() == "rectangle":
        return round(width * length, 2)
    else:
        return "Invalid shape"


if __name__ == "__main__":
    print(calculate_area("test"))
    print(calculate_area("circle", radius=3))
    print(calculate_area("rectangle", length=5, width=6))

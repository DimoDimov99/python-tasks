import math


def calculate_area(shape: str, radius=1, length=1, width=1):
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

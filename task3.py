def remove_div_by_5() -> list:
    """Docstring"""
    l = [num for num in range(1, 21) if num % 2 == 0]
    """
    for item in l[:]:  # for fixing index
        if item % 5 == 0:
            l.remove(item)
    return l
    """
    l_len = len(l)
    index = 0
    while index < l_len:
        # we adjust l_len if we pop, and increase in both case the the index variable
        if l[index] % 5 == 0:
            l.pop(index)
            l_len -= 1
            index += 1
        index += 1
    return l


if __name__ == "__main__":
    print(remove_div_by_5())

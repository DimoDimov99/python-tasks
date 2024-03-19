student_grades = {
    "Alice": 85,
    "Bob": 75,
    "Charlie": 90,
}


def calc_student_avg(students_dict: dict) -> float:
    """Docstring"""
    result = 0
    for _, value in students_dict.items():
        result += value
    return round(result / len(students_dict), 2)


if __name__ == "__main__":
    print(calc_student_avg(student_grades))

class Student:
    student_id_count = 1

    def __init__(
        self, first_name: str, last_name: str, student_id: int, age: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.age = age
        self.student_id_count += 1

    # @staticmethod
    # def create_student(
    #     first_name="Dimo", last_name="Test", student_id=student_id_count, age="21"
    # ):
    #     first_name = input("Enter first name: ")
    #     last_name = input("Enter last name: ")
    #     age = input("Enter Age: ")
    #     result = {
    #         "First name": first_name,
    #         "Last name": last_name,
    #         "Student ID": student_id,
    #         "Age": age,
    #     }
    #     Student.student_id_count += 1
    #     return result


class StudentManagement:
    students = {}

    def __init__(self) -> None:
        pass

    def search(self, student_id: int) -> int:
        if student_id not in self.students:
            return 0
        else:
            return 1

    def accept(self, Student):
        if self.search(Student.student_id):
            print(f"Student with id {Student.student_id} already exist.")
        self.students[Student.student_id] = {
            "f_name": Student.first_name,
            "l_name": Student.last_name,
            "id": Student.student_id,
            "age": Student.age,
        }

    def display(self, student_id: int):
        if self.search(student_id):
            print(
                f'{self.students[student_id]["f_name"]} {self.students[student_id]["l_name"]} is {self.students[student_id]["age"]}-years old and has and id of {self.students[student_id]["id"]}.'
            )
        else:
            print(f"Student with id {student_id} does not exist.")

    def delete(self, student_id: int):
        if self.search(student_id):
            self.students.pop(student_id)
            print(f"Student with id {student_id} removed.")
        else:
            return f"Student with id {student_id} does not exist."


if __name__ == "__main__":
    student1 = Student("John", "Doe", 1, 18)
    student2 = Student("Peter", "Oswell", 1, 15)
    student3 = Student("Lilliam", "Pumpernickle", 2, 22)
    student_management = StudentManagement()
    student_management.accept(student1)
    student_management.accept(student2)
    student_management.accept(student3)
    student_management.display(3)
    student_management.display(2)
    student_management.delete(1)
    student_management.display(1)

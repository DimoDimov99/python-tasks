class Student:

    def __init__(
        self, first_name: str, last_name: str, student_id: int, age: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.age = age

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
        self.students = []
        # pass

    def search(self, student_id: int) -> int:
        student = [student for student in self.students if student.student_id == student_id]
        if (student): # A empty list will return False
            return student[0]
        return False
        # if student_id not in self.students:
        #     return 0
        # else:
        #     return 1

    def accept(self, student): # The logic here is overcomplicated. You can actually pass the actual Student instances and put them in a list to filter there. You shouldn't re-declare the same values in the container class.
        student = self.search(student.student_id)
        if student:
            print(f"Student with id {student.student_id} already exist.")
        self.students.append(student)
        # if self.search(Student.student_id):
        #     print(f"Student with id {Student.student_id} already exist.")
        # self.students[Student.student_id] = {
        #     "f_name": Student.first_name,
        #     "l_name": Student.last_name,
        #     "id": Student.student_id,
        #     "age": Student.age,
        # }

    def display(self, student_id: int):
        student = self.search(student.student_id)
        if student
            print(
                f'{student.first_name} {student.last_name} is {student.age}-years old and has and id of {student.first_name.student_id}.'
            )
        else:
            print(f"Student with id {student_id} does not exist.")

    def delete(self, student_id: int):
        student = self.search(student.student_id)
        if student:
            self.students.pop(student)
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

from models.student import Student

class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 20:
            raise ValueError("Group cannot have more than 20 students")
        self.students.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.students.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        students_list = "\n".join(str(student) for student in self.students)
        return f"Group {self.name}:\n{students_list}"

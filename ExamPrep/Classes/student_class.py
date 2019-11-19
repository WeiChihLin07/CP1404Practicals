"""
Creat a Student class - derived from Person, also has student_id attribute
"""

from ExamPrep.Classes.person_class import Person


class Student(Person):
    def __init__(self, name='', age=0, student_id=''):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return "ID: {}".format(self.student_id, super().__str__())


jill = Student('Jill', 18, '126743')
print(jill)

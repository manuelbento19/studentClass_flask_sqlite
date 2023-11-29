import uuid

class Student:
    def __init__(self,firstName,lastName,course):
        self.id = uuid.uuid4().hex
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
    def __str__(self):
        return f'id:  {self.id}'\
        f'firstName: {self.firstName}'\
        f'lastName: {self.lastName}'\
        f'course: {self.course}'

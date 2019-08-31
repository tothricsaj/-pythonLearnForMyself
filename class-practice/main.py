class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        """
        Print the details of person
        """
        print('Name is {}'.format(self.name))
        print('Age is {}'.format(self.age))



class ClassLeader:
    def __init__(self, sum_class_members=None, class_specialized=None, is_class_leader=False):
        self.sum_class_members = sum_class_members
        self.class_specialized = class_specialized
        self.is_class_leader = is_class_leader

    def get_cl_details(self):
        print('Count of class members is {}'.format(self.sum_class_members))
        print('This class is specialized by {}'.format(self.class_specialized))



class Teacher(Person, ClassLeader):
    def __init__(self, name, age, teached_subject, sum_class_members=None, class_specialized=None, is_class_leader=False):
        Person.__init__(self, name, age)
        ClassLeader.__init__(self, sum_class_members, class_specialized, is_class_leader)
        self.teached_subject = teached_subject

    def get_details(self):
        print('This person is a teacher!')
        Person.get_details(self)
        print('The teacher teach this subject {}'.format(self.teached_subject))

        if self.is_class_leader:
            ClassLeader.get_cl_details(self)

if __name__ == "__main__":
    
    per1 = Person('Jhon Doo', 22)
    per1.get_details();

    print('\n')

    per2 = Teacher('Frank Einstein', 70, 'Biology', None, None, False)
    per2.get_details()

    print('\n')

    per3 = Teacher('Solder Sam', 43, 'Sport', 21, 'Engilsh', True)
    per3.get_details()

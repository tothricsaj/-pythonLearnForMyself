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



class Teacher(Person):
    def __init__(self, name, age, teached_subject):
        Person.__init__(self, name, age)
        self.teached_subject = teached_subject

    def get_details(self):
        print('This person is a teacher!')
        Person.get_details(self)
        print('The teacher teach this subject {})'.format(self.teached_subject))

if __name__ == "__main__":
    
    per1 = Person('Jhon Doo', 22)
    per1.get_details();

    print('\n')

    per2 = Teacher('Frank Einstein', 70, 'Biology')
    per2.get_details()

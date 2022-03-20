class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def contact(self):
        print(self.name, 'has made contact')

    def print_details(self):
        print(self.name, 'is', self.age, 'years old. ', end = '')

    def change_name(self, new_name):
        if new_name != '':
            print(self.name, 'is changing their name.', end = '')
            self.name = new_name
            print('Their new name is', self.name)

    def change_age(self, new_age):
        if new_age > self.age:
            print(self.name, self.age, 'is changing their age.', end = '')
            self.age = new_age
            print('Their new age is', new_age)
        else:
            print(self.name, 'you cannot get younger in age.')

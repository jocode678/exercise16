from person import Person

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self._employeeID = employeeID

    # This is polymorphism because I am overwriting the request in the person Class?
    def contact(self):
        print(self.name, self._employeeID, 'has responded to a request')

    def print_details(self):
        super().print_details()
        print('Their Employee ID is', self._employeeID)






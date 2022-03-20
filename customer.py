from person import Person

class Customer(Person):
    def __init__(self, name, age, customerID):
        super().__init__(name, age)
        self._customerID = customerID

    # This is polymorphism because I am overwriting the request in the person Class?
    def contact(self):
        print(self.name, self._customerID, 'has made a request')

    def print_details(self):
        super().print_details()
        print('Their customer ID is', self._customerID)


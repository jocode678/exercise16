from person import Person
from customer import Customer
from employee import Employee
from bank_account import Bank_account

person1 = Person('Holly Wright', 29)

customer1 = Customer('Jack Brown', 32, 'C01')
customer2 = Customer('Helen Green', 43, 'C02')

employee1 = Employee('Jade Smith', 34, 'E01')
employee2 = Employee('Matt Far', 42, 'E02')

customer1.print_details()
customer2.print_details()
employee1.print_details()
employee2.print_details()

print('---')

person1.contact()
customer1.contact()
employee1.contact()

print('---')

person1.change_name('Holly White')
customer1.change_name('Jackson Brown')
employee1.change_name('Jade Smithy')
person1.change_name('Holly Whittle')
person1.change_age(33)
customer2.change_age(22)
employee2.change_age(47)
employee2.print_details()

print('---')

# This changed their customer ID which I didn't want it to do
customer1 = Customer('Jack Brown', 33, '404')
customer1.print_details()

# This also changes their customer ID which I didn't want it to do
customer1._customerID = '555'
customer1.print_details()

print('---')
person3 = Person('Person three', 32)

account1 = Bank_account('Person three', 32, 11112222, 'ISA', 100.00)
person3.print_details()
account1.account_info()
account1.balance_enquiry()
account1.deposit_money(50)
account1.deposit_money(50)

account1.withdraw_money(300)
account1.withdraw_money(100)



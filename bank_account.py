from person import Person

class Bank_account(Person):
    # Can you put an object into here (eg Person three) so you can link person to account without
    # re-typing their information?
    def __init__ (self, name, age, account_number, type, balance):
        super().__init__(name, age)
        self.account_number = account_number
        self.type = type
        self.balance = balance

    def account_info(self):
        print('The account number is', self.account_number, 'the account type is', self.type, 'the balance is', self.balance)

    def balance_enquiry(self):
        print('Bank account', self.account_number, 'has a balance of £', self.balance)

    def deposit_money(self, deposit_amount):
        print('The bank balance was £', self.balance, '. ', end ='')
        self.balance += deposit_amount
        print('A deposit of £', deposit_amount, 'was made. The updated bank balance is £', self.balance)

    def withdraw_money(self, withdraw_amount):
        print('Your bank balance is £', self.balance, '. ', end = '')
        if self.balance > withdraw_amount:
            self.balance -= withdraw_amount
            print('£', withdraw_amount, 'has been withdrawn. Your new balance is £', self.balance)
        else:
            print('You do not have enough money in your account to withdraw £', withdraw_amount)



import time

class Atm:
    def __init__(self, pin, balance):
        # Initialize the ATM with a PIN and a balance.
        self.pin = pin
        self.balance = balance
        self.history = {}  # Dictionary to keep transaction history.
        self.services()  # Start the ATM services.
        
    def services(self):
        # Main menu loop for ATM services.
        while True:
            try:
                options = int(input('''
                    Enter 1 for Balance Inquiry
                    Enter 2 for Withdrawal
                    Enter 3 for Deposit
                    Enter 4 for Pin Change
                    Enter 5 for Transaction History
                    Enter 0 to Exit
                    '''))
                # Call the appropriate method based on user input.
                if options == 1:
                    time.sleep(1)
                    self.balance_inquiry()
                elif options == 2:
                    time.sleep(1)
                    self.withdraw()
                elif options == 3:
                    time.sleep(1)
                    self.deposit()
                elif options == 4:
                    time.sleep(1)
                    self.pin_change()
                elif options == 5:
                    time.sleep(1)
                    self.transaction_history()
                elif options == 0:
                    time.sleep(1)
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print('Invalid input')
                break        
    
    def balance_inquiry(self):
        # Print the current balance.
        print('Your current balance is: ', self.balance)
    
    def withdraw(self):
        # Handle the withdrawal process.
        amount = int(input('Enter Amount: '))
        if amount <= self.balance:
            self.balance -= amount
            self.history[time.time()] = f'{amount} was withdrawn'
            time.sleep(2)
            print('Amount deducted')
        else:
            print('Insufficient balance')
        time.sleep(1)
        print('Your current balance is: ', self.balance)
        
    def deposit(self):
        # Handle the deposit process.
        amount = int(input('Enter Amount: '))
        time.sleep(2)
        print(amount, 'added to your previous balance')
        time.sleep(1)
        self.balance += amount
        self.history[time.time()] = f'{amount} was deposited'
        print('Your current balance is: ', self.balance)

    def pin_change(self):
        # Handle the PIN change process.
        curr_pin = int(input('Enter current pin: '))
        if curr_pin == self.pin:
            time.sleep(1)
            new_pin = int(input('Enter new pin: '))
            self.pin = new_pin
            time.sleep(2)
            print('Your pin has been updated successfully.')
        else:
            print('Invalid pin')
            time.sleep(1)
    
    def transaction_history(self):
        # Print the transaction history.
        for timestamp, action in self.history.items():
            print(f'{time.ctime(timestamp)}: {action}')

# Create an ATM object with a PIN and initial balance.
obj = Atm(123, 10000)

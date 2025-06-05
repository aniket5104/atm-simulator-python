class ATM:
    def __init__(self):
        self.__pin=""
        self.__balance=50000
        self.create_Pin()
        self.menu()
    
    def menu(self):
        while True:
            user_input=input("""
            Hello! How would you like to proceed?
            1. Change PIN
            2. Deposit Money
            3. Withdraw money
            4. check Balance
            5. Exit
            """)
        
            if user_input=="1":
                self.create_Pin()
            elif user_input=="2":
                self.deposit_Money()
            elif user_input=="3":
                self.withdraw_money()
            elif user_input=="4":
                self.check_Bal()
            elif user_input=="5":
                self.exit()
            else:
                print("Please enter a valid number from the MENU!")

    def create_Pin(self):
        temp=input("Enter the PIN(4-digit): ")
        if temp.isdigit() and len(temp)==4:
            self.__pin=temp
            print("PIN set!")
        else:
            print("Invalid PIN format")
            exit()
    
    def deposit_Money(self):
        temp=input("Enter Your PIN: ")
        if temp==self.__pin:
            depo_amount=int(input("Enter the amount to be deposited: "))
            self.__balance+=depo_amount
            print("Deposit Successful!")
            print("Balance=",self.__balance)
        else:
            print("You entered a wrong pin")
    
    def withdraw_money(self):
        temp=input("Enter your PIN: ")
        if temp==self.__pin:
            with_amount=int(input("Enter the amount to be withdrawn: "))
            if with_amount<=0:
                print("Please enter a valid Withdrawal amount")
            elif self.__balance>= with_amount:     
                self.__balance-=with_amount
                print("Transaction Successful")
                print("Available Balance:",self.__balance)
            else :
                print("Insufficient Funds")
        else:
            print("You entered a wrong PIN")
    
    def check_Bal(self):
        temp=input("Enter your PIN: ")
        if temp==self.__pin:
            print("Your balance is",self.__balance)
        else:
            print("You entered a wrong pin")
    def exit(self):
        print("Bye! Have a nice day!")
        exit()
sbi=ATM()
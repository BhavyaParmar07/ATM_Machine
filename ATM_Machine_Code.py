# Creating a class for the functions.
class ATM_Machine:
# Displaying the ATM_Menu.
    def atm_menu(self):
        atm_menu_list = [
            "\n============== ATM Menu ==============",
            "Check Balance -- C",
            "Deposite -- D",
            "Withdraw -- W",
            "Quit -- Q",
            "--------------------------------------"
        ]
        for i in atm_menu_list:
            print(i)

# Asking the user for the Menu_Mode & Printing accodingly.
    def menu_input(self):
        while True:
            self.check_menu_1 = input("\nEnter Your Choice : ").lower()
            print("--------------------------------------")
            if (self.check_menu_1 == "c"):
                acc_1.user_balance_input()
            elif (self.check_menu_1 == "d"):
                acc_1.user_deposite_input()
            elif (self.check_menu_1 == "w"):
                acc_1.user_withdraw_input()
            elif (self.check_menu_1 == "q"):
                break
            else:
                print("--------------------------------------")
                print("Error : This menu is not here")
                print("--------------------------------------")
# Creating a Account Here.
    def account(self, acc_no, acc_pin, balance):
        self.acc_no = acc_no
        self.acc_pin = acc_pin
        self.balance = balance
        
# This is the function for Checking the balance.
    def user_balance_input(self):
        while True:
            self.user_acc_no = int(input("\nEnter Your Account_no : "))
            self.user_acc_pin = int(input("Enter Your Account_Pin_no : "))
        
            if ((self.user_acc_no == self.acc_no) and (self.user_acc_pin == self.acc_pin)):
                print("Remening Balance : ", self.balance)
                print("--------------------------------------")
                break
            else:
                print("--------------------------------------")
                print("Error : Anyone of the input is incorrect.\nplease try again")
                print("--------------------------------------")

# This is the function for Depositing the money.
    def user_deposite_input(self):
        while True:
            self.user_acc_no = int(input("\nEnter Your Account_no : "))
            self.user_acc_pin = int(input("Enter Your Account_Pin_no : "))
            self.user_deposite_amo = int(input("Enter Your Deposite_Amount : "))
        
            if ((self.user_acc_no == self.acc_no) and (self.user_acc_pin == self.acc_pin)):
                self.balance += self.user_deposite_amo
                print("Updated Balance : ", self.balance)
                print("--------------------------------------")
                break
            else:
                print("--------------------------------------")
                print("Error : Anyone of the input is incorrect.\nplease try again")
                print("--------------------------------------")

# This is the function for Withdrawing the money.
    def user_withdraw_input(self):
        while True:
            self.user_acc_no = int(input("\nEnter Your Account_no : "))
            self.user_acc_pin = int(input("Enter Your Account_Pin_no : "))
            self.user_withdrawal_amo = int(input("Enter Your Withdrawal_Amount : "))
        
            if ((self.user_acc_no == self.acc_no) and (self.user_acc_pin == self.acc_pin) and (self.user_withdrawal_amo <= self.balance)):
                self.balance -= self.user_withdrawal_amo
                print("Updated Balance : ", self.balance)
                print("--------------------------------------")
                break
            elif(self.user_withdrawal_amo >= self.balance):
                print("--------------------------------------")
                print(f"Error : You only have {self.balance} to withdraw.")
                print("--------------------------------------")
            else:
                print("--------------------------------------")
                print("Error : Anyone of the input is incorrect.\nplease try again")
                print("--------------------------------------")
                
acc_1 = ATM_Machine()
# This function is for calling all the function at one's.
def main(): 
    acc_1.atm_menu()
    acc_1.account(15335122, 159753, 25000)
    acc_1.menu_input()

main()
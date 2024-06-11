from cardHolder import cardHolder

def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much amount you would like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank You for your amount. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid Input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much amount you would like to withdraw: "))
        ### check if user has enough money
        if(cardHolder.get_balance()< withdraw):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank You :)")
    except:
        print("Invalid Input")

def check_balance(cardHolder):
    print("Your current balance is:", cardHolder.get_balance())

if __name__ == "__main__":
      current_user = cardHolder("","","","","")

      ###create a repo of cardholders:
      list_of_cardHolders = []
      list_of_cardHolders.append(cardHolder("4575638758783750857", 1234, "Anjali", "Deshwal", 150.31))
      list_of_cardHolders.append(cardHolder("4575638758745678858", 2345, "Manisha", "Vaishnav", 321.13))
      list_of_cardHolders.append(cardHolder("4572343558783750856", 3456, "Neha", "Saini", 105.59))
      list_of_cardHolders.append(cardHolder("4575635558783750854", 4567, "Tanisha", "Smith", 54.27))
      list_of_cardHolders.append(cardHolder("4575698768783750857", 5678, "Vandana", "Sheoraan", 851.34))

      ###prompt user for debit card number
      debitCardNum = ""
      while True:
          try:
              debitCardNum = input("Please inser your debit card: ")
              ### check against repo
              debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
              if(len(debitMatch) > 0):
                  current_user = debitMatch[0]
                  break
              else: 
                  print("Card number not recognized. Please try again.")
          except:
              print("Card number not recognized. Please try again.")
        
        ### Prompt for PIN
      while True:
          try:
              userPin = int(input("Please enter your pin: ").strip())
              if(current_user.get_pin() == userPin):
                  break
              else:
                  print("Invalid PIN. Please try again.")
          except:
               print("Invalid PIN. Please try again.")

    ### Print Options
print("Welcome ", current_user.get_firstname(), " :)")
option = 0
while (option != 4):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid Input. Please try again.")
        
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
    
print("Thank You. Have a nice day :)")
      

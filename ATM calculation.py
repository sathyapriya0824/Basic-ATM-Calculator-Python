balance = 10000 

print("ATM MENU")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice (1-3): "))
if choice == 1:
 print("Your current balance is:", balance)
elif choice == 2:
 deposit = int(input("Enter amount to deposit: "))
 balance = balance + deposit 
 print("Amount deposited successfully!")
 print("Updated balance:", balance)
elif choice == 3:
 withdraw = int(input("Enter amount to withdraw: "))
 if withdraw <= balance: 
 balance = balance - withdraw 
 print("Please collect your cash")
 print("Remaining balance:", balance)
 else:
 print("Insufficient balance!")
else:
 print("Invalid choice! Try again.")


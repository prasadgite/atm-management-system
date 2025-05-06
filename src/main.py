import os
from colorama import init, Fore, Style
from tabulate import tabulate
from src.user import User
from src.database import DatabaseConnection

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════╗
    ║         ATM Management System         ║
    ╚═══════════════════════════════════════╝
    """ + Style.RESET_ALL)

def get_input(prompt, input_type=str):
    while True:
        try:
            value = input(prompt)
            if input_type == int:
                return int(value)
            return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

def main_menu():
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")
    return get_input("Select an option (1-3): ", int)

def user_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Logout")
    return get_input("Select an option (1-5): ", int)

def main():
    db = DatabaseConnection()
    user_manager = User()
    
    try:
        db.connect()
        
        while True:
            clear_screen()
            print_header()
            
            choice = main_menu()
            
            if choice == 1:  # Login
                username = input("Enter username: ")
                password = input("Enter password: ")
                
                success, result = user_manager.login(username, password)
                if success:
                    print(Fore.GREEN + "\nLogin successful!" + Style.RESET_ALL)
                    user_data = result
                    
                    while True:
                        choice = user_menu()
                        
                        if choice == 1:  # Check Balance
                            balance = user_manager.get_balance(user_data['user_id'])
                            print(f"\nCurrent Balance: ${balance:.2f}")
                            
                        elif choice == 2:  # Deposit
                            amount = get_input("Enter amount to deposit: $", float)
                            success, message = user_manager.update_balance(
                                user_data['user_id'], amount, 'DEPOSIT'
                            )
                            print(Fore.GREEN + message + Style.RESET_ALL if success else Fore.RED + message + Style.RESET_ALL)
                            
                        elif choice == 3:  # Withdraw
                            amount = get_input("Enter amount to withdraw: $", float)
                            success, message = user_manager.update_balance(
                                user_data['user_id'], -amount, 'WITHDRAWAL'
                            )
                            print(Fore.GREEN + message + Style.RESET_ALL if success else Fore.RED + message + Style.RESET_ALL)
                            
                        elif choice == 4:  # Transaction History
                            transactions = user_manager.get_transaction_history(user_data['user_id'])
                            if transactions:
                                headers = ["Type", "Amount", "Balance After", "Date"]
                                print("\nTransaction History:")
                                print(tabulate(transactions, headers=headers, tablefmt="grid"))
                            else:
                                print("\nNo transactions found.")
                                
                        elif choice == 5:  # Logout
                            print(Fore.YELLOW + "\nLogging out..." + Style.RESET_ALL)
                            break
                            
                else:
                    print(Fore.RED + f"\n{result}" + Style.RESET_ALL)
                    
            elif choice == 2:  # Register
                username = input("Enter username: ")
                password = input("Enter password: ")
                full_name = input("Enter full name: ")
                
                success, message = user_manager.register_user(username, password, full_name)
                print(Fore.GREEN + message + Style.RESET_ALL if success else Fore.RED + message + Style.RESET_ALL)
                
            elif choice == 3:  # Exit
                print(Fore.YELLOW + "\nThank you for using ATM Management System!" + Style.RESET_ALL)
                break
                
            input("\nPress Enter to continue...")
            
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {str(e)}" + Style.RESET_ALL)
    finally:
        db.disconnect()

if __name__ == "__main__":
    main() 
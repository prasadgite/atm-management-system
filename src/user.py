import bcrypt
import random
import string
from src.database import DatabaseConnection

class User:
    def __init__(self):
        self.db = DatabaseConnection()

    def generate_account_number(self):
        """Generate a unique 10-digit account number"""
        while True:
            account_number = ''.join(random.choices(string.digits, k=10))
            # Check if account number exists
            query = "SELECT id FROM users WHERE account_number = %s"
            result = self.db.fetch_one(query, (account_number,))
            if not result:
                return account_number

    def register_user(self, username, password, full_name):
        """Register a new user with hashed password"""
        try:
            # Check if username exists
            query = "SELECT id FROM users WHERE username = %s"
            if self.db.fetch_one(query, (username,)):
                return False, "Username already exists"

            # Hash password
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Generate account number
            account_number = self.generate_account_number()

            # Insert new user
            query = """
                INSERT INTO users (username, password_hash, full_name, account_number)
                VALUES (%s, %s, %s, %s)
            """
            self.db.execute_query(query, (username, password_hash, full_name, account_number))
            return True, f"Registration successful. Your account number is: {account_number}"
        except Exception as e:
            return False, f"Registration failed: {str(e)}"

    def login(self, username, password):
        """Authenticate user login"""
        try:
            query = "SELECT id, password_hash, full_name, account_number, balance FROM users WHERE username = %s"
            result = self.db.fetch_one(query, (username,))
            
            if not result:
                return False, "Invalid username or password"

            user_id, stored_hash, full_name, account_number, balance = result
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                return True, {
                    'user_id': user_id,
                    'full_name': full_name,
                    'account_number': account_number,
                    'balance': balance
                }
            return False, "Invalid username or password"
        except Exception as e:
            return False, f"Login failed: {str(e)}"

    def get_balance(self, user_id):
        """Get user's current balance"""
        try:
            query = "SELECT balance FROM users WHERE id = %s"
            result = self.db.fetch_one(query, (user_id,))
            return result[0] if result else None
        except Exception as e:
            print(f"Error getting balance: {e}")
            return None

    def update_balance(self, user_id, amount, transaction_type):
        """Update user's balance and record transaction"""
        try:
            # Get current balance
            current_balance = self.get_balance(user_id)
            if current_balance is None:
                return False, "User not found"

            # Calculate new balance
            new_balance = current_balance + amount if transaction_type == 'DEPOSIT' else current_balance - amount
            
            if new_balance < 0:
                return False, "Insufficient funds"

            # Update balance
            query = "UPDATE users SET balance = %s WHERE id = %s"
            self.db.execute_query(query, (new_balance, user_id))

            # Record transaction
            query = """
                INSERT INTO transactions (user_id, transaction_type, amount, balance_after)
                VALUES (%s, %s, %s, %s)
            """
            self.db.execute_query(query, (user_id, transaction_type, abs(amount), new_balance))
            
            return True, f"Transaction successful. New balance: {new_balance}"
        except Exception as e:
            return False, f"Transaction failed: {str(e)}"

    def get_transaction_history(self, user_id):
        """Get user's transaction history"""
        try:
            query = """
                SELECT transaction_type, amount, balance_after, transaction_date
                FROM transactions
                WHERE user_id = %s
                ORDER BY transaction_date DESC
                LIMIT 10
            """
            return self.db.fetch_all(query, (user_id,))
        except Exception as e:
            print(f"Error getting transaction history: {e}")
            return [] 
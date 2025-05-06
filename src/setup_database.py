import mysql.connector
from mysql.connector import Error

def setup_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='3396404y'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS atm_management")
            cursor.execute("USE atm_management")
            
            # Create users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    full_name VARCHAR(100) NOT NULL,
                    account_number VARCHAR(20) UNIQUE NOT NULL,
                    balance DECIMAL(10,2) DEFAULT 0.00,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """)
            
            # Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    transaction_type ENUM('DEPOSIT', 'WITHDRAWAL') NOT NULL,
                    amount DECIMAL(10,2) NOT NULL,
                    balance_after DECIMAL(10,2) NOT NULL,
                    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            
            # Create indexes (wrapped in try-except as they might already exist)
            try:
                cursor.execute("CREATE INDEX idx_username ON users(username)")
            except Error:
                pass
                
            try:
                cursor.execute("CREATE INDEX idx_account_number ON users(account_number)")
            except Error:
                pass
                
            try:
                cursor.execute("CREATE INDEX idx_transaction_date ON transactions(transaction_date)")
            except Error:
                pass
            
            print("Database and tables created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    setup_database() 
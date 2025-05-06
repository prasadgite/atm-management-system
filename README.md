
# ATM Management System

A secure and efficient ATM Management System built with Python and MySQL, featuring a modern command-line interface with color-coded output and comprehensive transaction management.

## 🌟 Features

### Core Functionality
- **User Management**
  - Secure user registration with unique account numbers
  - Password-protected login system
  - User profile management
  - Account balance tracking

### Financial Operations
- **Transaction Management**
  - Real-time balance checking
  - Secure deposit operations
  - Withdrawal with balance validation
  - Transaction history with detailed records
  - Last 10 transactions display

### Security Features
- **Advanced Security**
  - Password hashing using bcrypt
  - SQL injection prevention
  - Input validation and sanitization
  - Secure database connections
  - Environment variable configuration
  - Transaction rollback on errors

### User Interface
- **Modern CLI Interface**
  - Color-coded output using colorama
  - Tabulated transaction history
  - Clear menu navigation
  - Intuitive user prompts
  - Error message formatting

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
  - Object-oriented programming
  - Exception handling
  - Singleton pattern for database connection
  - Modular code structure

### Database
- **MySQL**
  - Relational database management
  - Transaction support
  - Indexed queries for performance
  - Foreign key constraints
  - Timestamp tracking

### Dependencies
- **Core Libraries**
  - `mysql-connector-python`: Database connectivity
  - `python-dotenv`: Environment variable management
  - `bcrypt`: Password hashing
  - `colorama`: Terminal text coloring
  - `tabulate`: Formatted table output

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server 8.0 or higher
- Git (for version control)
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository:**

git clone https://github.com/yourusername/atm-management-system.git
cd atm-management-system

2. **Create and activate virtual environment (recommended):**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install required packages:**

pip install -r requirements.txt


4. **Database Setup:**
   - Create a MySQL database named `atm_management`
   - Run the SQL script in `database/setup.sql`
   
   mysql -u root -p < database/setup.sql
   

5. **Environment Configuration:**
   - Copy `.env.example` to `.env`
   - Update the database credentials:
   
   DB_HOST=localhost
   DB_NAME=atm_management
   DB_USER=your_username
   DB_PASSWORD=your_password
   

## 💻 Usage

1. **Start the application:
python src/main.py


2. **Main Menu Options:**
   - Login to existing account
   - Register new account
   - Exit application

3. **User Menu Options:**
   - Check Balance
   - Deposit Money
   - Withdraw Money
   - View Transaction History
   - Logout

## 📁 Project Structure


atm-management-system/
├── src/
│   ├── main.py           # Main application entry point
│   ├── database.py       # Database connection management
│   ├── user.py          # User operations and authentication
│   └── utils.py         # Utility functions
├── database/
│   └── setup.sql        # Database schema and setup
├── tests/
│   └── test_main.py     # Unit tests
├── .env.example         # Environment variables template
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation


## 🔒 Security Implementation

- **Password Security**
  - Bcrypt hashing with salt
  - Secure password storage
  - Password validation

- **Database Security**
  - Parameterized queries
  - Connection pooling
  - Transaction management
  - Error handling and rollback

- **Input Validation**
  - Type checking
  - Range validation
  - Format verification
  - Error handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by real-world ATM systems
- Built for educational purposes 

# atm-management-system
Secure and modern command-line ATM system with Python and MySQL

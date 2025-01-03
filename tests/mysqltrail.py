from datetime import datetime
from numbers import Number
from tkinter.constants import CURRENT

import pymysql.cursors
from pymysql.cursors import Cursor


# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)

class DBConnection:

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Password@2024',
            db='sample'
        )
        self.create_table()

    def create_table(self):
        try:
            with self.connection.cursor() as cursor:
                sql = """CREATE TABLE IF NOT EXISTS USERS (
                    ACCOUNT_NO INT PRIMARY KEY,
                    NAME VARCHAR(15),
                    PASSWORD VARCHAR(25),  
                    AGE INT,
                    EMAIL VARCHAR(50) UNIQUE NOT NULL,
                    BALANCE DECIMAL(10, 2) DEFAULT 0.00
                );"""
                cursor.execute(sql)
                # self.connection.commit()  # Commit the changes
        except Exception as e:
            print(f"Error creating table: {e}")

    def get_next_account_number(self):
        try:
            with self.connection.cursor() as cursor:
                sql= "SELECT MAX(ACCOUNT_NO) FROM USERS;"
                cursor.execute(sql)
                result = cursor.fetchone()
                if result[0] is not None:
                    return result[0] + 1  # Increment the max account number
                else:
                    return 1000
        except Exception as e:
            print(f"Error fetching next account number: {e}")
            return None

    def save_account(self, account_number, name, password, age, email, balance):
        try:
            with self.connection.cursor() as cursor:
                sql = """INSERT INTO USERS (
                    ACCOUNT_NO,
                    NAME,
                    PASSWORD,
                    AGE,
                    EMAIL,
                    BALANCE
                ) VALUES (%s, %s, %s, %s, %s, %s);"""  # Fixed SQL syntax
                cursor.execute(sql, (account_number, name, password, age, email, balance))
                self.connection.commit()  # Commit the changes
        except Exception as e:
            print(f"Error saving account: {e}")

    def login(self, account_number, password):
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT ACCOUNT_NO FROM USERS WHERE 
                ACCOUNT_NO= %s AND PASSWORD= %s
                """
                cursor.execute(sql, (account_number, password))
                result = cursor.fetchone()
                if result is not None:
                    return result[0], True
                else:
                    return None, False
        except Exception as e:
            print(f"Error logging in account: {e}")

    def check_balance(self, account_number):
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT BALANCE FROM USERS WHERE 
                ACCOUNT_NO= %s
                """
                cursor.execute(sql, (account_number))
                result = cursor.fetchone()
                if result is not None:
                    balance= result[0]
                    return balance

        except Exception as e:
            print(f"Error in getting account balance: {e}")


    def withdraw(self, account_number, amount):
        if not isinstance(account_number, Number) or not isinstance(amount, Number):
            return
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT BALANCE FROM USERS WHERE 
                ACCOUNT_NO= %s
                """
                cursor.execute(sql, account_number)
                result = cursor.fetchone()
                if result is not None:
                    balance2= result[0]
                    if result[0]< amount:
                        print(f"Amount {amount} is greater than {balance2}")
                        return
                    else:
                        balance2= balance2 - amount
                        print(balance2)
                        # update_amount(account_number, balance)
                        sql2= """UPDATE USERS SET BALANCE= %s WHERE
                        ACCOUNT_NO= %s
                        """
                        cursor.execute(sql2, (balance2, account_number))
                        self.connection.commit()
                        return True
        except Exception as e:
            print(f"Error in getting account balance: {e}")

    def deposit(self, account_number, amount):
        if not isinstance(account_number, Number) or not isinstance(amount, Number):
            return
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT BALANCE,NAME, AGE FROM USERS WHERE 
                ACCOUNT_NO= %s
                """
                cursor.execute(sql, account_number)
                result = cursor.fetchone()
                if result is not None:
                    balance2= result[0]
                    balance2= balance2 + amount
                    print(balance2)
                    # update_amount(account_number, balance)
                    sql2= """UPDATE USERS SET BALANCE= %s WHERE
                    ACCOUNT_NO= %s
                    """
                    cursor.execute(sql2, (balance2, account_number))
                    self.connection.commit()
                    return True
        except Exception as e:
            print(f"Error in getting account balance: {e}")

    def transfer_money(self, sender_account_no):
        receiver_account_number = input("Enter receiver's account number: ")
        amount = int(input("Enter amount to transfer: "))
        try:
            with self.connection.cursor() as cursor:
                sql= """SELECT BALANCE FROM USERS WHERE ACCOUNT_NO= %s"""
                cursor.execute(sql, sender_account_no)
                sender= cursor.fetchone()
                if sender is not None:
                    sql2= """SELECT BALANCE FROM USERS WHERE ACCOUNT_NO= %s"""
                    cursor.execute(sql2, receiver_account_number)
                    receiver= cursor.fetchone()
                    if receiver is not  None:
                        sender_balance= sender[0]- amount
                        receiver_balance= receiver[0]+ amount
                        print(sender_balance,receiver_balance)
                        update_recbalance_query= """UPDATE USERS SET BALANCE= %s WHERE ACCOUNT_NO= %s"""
                        update_sendbalance_query= """UPDATE USERS SET BALANCE= %s WHERE ACCOUNT_NO= %s"""
                        cursor.execute(update_recbalance_query, (receiver_balance, receiver_account_number))
                        cursor.execute(update_sendbalance_query, (sender_balance, sender_account_no))
                        self.connection.commit()
                        return True
                    else:
                        print("Invalid receiver account no")
                        return False
                else:
                    print("Invalid sender account no")
                    return False
        except Exception as e:
            print(f"Error in getting account no: {e}")


    def store_transaction(self, account_number, transaction_type, amount):
        try:
            with self.connection.cursor() as cursor:
                sql = """CREATE TABLE IF NOT EXISTS TRANSACTION (
                    TRANSACTION_ID INT AUTO_INCREMENT,
                    ACCOUNT_NO INT,
                    DATE DATETIME,
                    TRANSACTION_TYPE VARCHAR(25),  
                    AMOUNT INT,
                    PRIMARY KEY(TRANSACTION_ID)
                );"""
                cursor.execute(sql)

                sql2= """INSERT INTO TRANSACTION(ACCOUNT_NO, DATE, TRANSACTION_TYPE, AMOUNT) VALUES(%s, CURRENT_TIMESTAMP(), %s, %s)"""
                cursor.execute(sql2,(account_number, transaction_type, amount))
                self.connection.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    # def update_amount(self,aa):
    def log_transaction(self,account_number, transaction_type, amount):

        """
        Logs a transaction by storing it with the current date.

        Args:
            account_number (int): The account_number on which the operation is done
            transaction_type (str): The type of transaction (e.g., 'Debit' or 'Credit').
            amount (float): The amount of the transaction.
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.store_transaction(account_number, date, transaction_type, amount)

    def get_transaction_history(self, account_number):
        """
        Retrieves the transaction history for a specific account.

        Args:
            account_number (str): The account number for which to retrieve the transaction history.

        Returns:
            list: A list of transactions associated with the account number.
        """

        transactions = []
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM TRANSACTION WHERE ACCOUNT_NO = %s"
                cursor.execute(sql, (account_number,))  # Pass as a tuple
                result = cursor.fetchall()
                print(result)
                print(len(result))
                for entry in result:
                    transactions.append(entry[3:7])
                return transactions
        except Exception as e:
            print(f"Error retrieving transaction history: {e}")

    def close(self):
        if self.connection:
            self.connection.close()


db = DBConnection()
try:
    # account_number= db.get_next_account_number()
    # db.save_account(account_number, "Tho", "kjnjnjn", 22, "ssn@example.com", 100.00)
    # db.save_account(account_number, "Thooo", "kjnjnjn", 22, "resh@yash.com", 10000.00)
    # acc_no,auth= db.login(100,'kjnjnjn')
    # print(acc_no,auth)

    # balance= db.check_balance(1003)
    # print(balance)
    # db.deposit(1003,52)
    # db.transfer_money(1000,1001,100)
    # balance= db.check_balance(1003)
    # print(balance)

    # db.store_transaction(1000, "Debit",100)
    # db.store_transaction(1010, "Debit", 100)
    print(db.get_transaction_history(1003))

finally:
    db.close()
import pickle

# Write a function in Python to count and display the total number of words in a text file.
from itertools import count


def count_words_in_file(file_path):
    """Counts and displays the total number of words in a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            total_words = len(words)
            print(f'Total number of words in the file: {total_words}')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

# count_words_in_file()
count_words_in_file("question_1.txt")


# count_words_in_file()

# Write a function in Python to read lines from a text file "notes.txt".
# Your function should find and display the occurrence of the word "the".
# For example: If the content of the file is:
# "India is the fastest-growing economy. India is looking for more
# investments around the globe. The whole world is looking at India as a great
# market. Most of the Indians can foresee the heights that India is capable of reaching."

def count_occurrences_of_the(file_path):
    """Counts and displays the occurrences of the word 'the' in a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_lower = text.lower()
            words = text_lower.split()
            # Count occurrences of the word 'the'
            count_the = words.count('the')
            print(f'The word "the" occurs {count_the} times in the file.')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

count_occurrences_of_the("the")

# 3.Write a function display_words() in python to read lines from a
# text file "story.txt", and display those words,
# which are less than 4 characters.
def display_words(file_path):
    """Reads lines from a text file and displays words that are less than 4 characters long."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                # Filter and display words that are less than 4 characters
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word,end=", ")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

display_words("story.txt")

# 4.Write a function in Python to count the words "this" and
# "these" present in a text file "article.txt".
# [Note that the words "this" and "these" are complete words]
def count_specific_words(file_path):
    """Counts and displays the occurrences of the words 'this' and 'these' in a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_lower = text.lower()
            words = text_lower.split()
            # Count occurrences of 'this' and 'these'
            count_this = words.count('this')
            count_these = words.count('these')
            print(f'The word "this" occurs {count_this} times in the file.')
            print(f'The word "these" occurs {count_these} times in the file.')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

count_specific_words("notes.txt")

# 4.Write a function in Python to count uppercase character in a text file.
def count_uppercase_characters(file_path):
    """Counts and displays the number of uppercase characters in a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            count=0
            text = file.read()
            file = text.split("")
            for data in file:
                if data.isupper():
                    count += 1
            print(f'The number of uppercase characters in the file is {count}.')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

count_uppercase_characters("notes.txt")

# 6. Aditi has used a text editing software to type some text.
# After saving the article as WORDS.TXT, she realised that she has wrongly typed alphabet J
# in place of alphabet I everywhere in the article.
# Write a function definition for JTOI() in Python that would display the corrected version
# of entire content of the file WORDS.
# TXT with all the alphabets "J" to be displayed as an alphabet "I" on screen.
# Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.

# Example: If Aditi has stored the following content in the file
# WORDS.TXT: WELL, THJS JS A WORD BY JTSELF.
# YOU COULD STRETCH THJS TO BE A SENTENCE The function JTOI() should display the following content:
def JTOI(file_path):
    """Reads the content of WORDS.TXT, replaces 'J' with 'I', and displays the corrected text."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Replace 'J' with 'I'
            corrected_content = content.replace('J', 'I')
            # Display the corrected content
            print(corrected_content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

JTOI("words.txt")


# A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# i. Write a user defined function createFile() to input data
# for a record and add to Book.dat.
# ii. Write a function countRec(Author) in Python which accepts the Author
# name as parameter and count and return number of
# books by the given Author are stored in the binary file "Book.dat"


class Book:
    def __init__(self, book_no, book_name, author, price):
        self.book_no = book_no
        self.book_name = book_name
        self.author = author
        self.price = price


def createFile():
    with open("Book.dat", "ab") as file:  # Open file in append binary mode
        book_no = int(input("Enter Book Number: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Price: "))

        book = Book(book_no, book_name, author, price)
        pickle.dump(book, file)  # Serialize and write the book object to file


def countRec(author):
    count = 0
    try:
        with open("Book.dat", "rb") as file:  # Open file in read binary mode
            while True:
                try:
                    book = pickle.load(file)  # Deserialize the book object
                    if book.author.lower() == author.lower():  # Case insensitive comparison
                        count += 1
                except EOFError:
                    break  # End of file reached
    except FileNotFoundError:
        print("The file 'Book.dat' does not exist.")
    return count

# createFile()
print(countRec("Tom"))

# A binary file "student.dat" has structure (admission_number, Name, Percentage).
# Write a function count_rec() in Python that would read contents of the file
# "STUDENT.DAT" and display the details of those students whose percentage is above 75.
# Also display number of students scoring above 75%.

def add_student_record():
    admission_number = input("Enter Student Code: ")
    name = input("Enter Student Name: ")
    Percentage = float(input("Enter Student Salary: "))

    # Create a dictionary for the employee record
    student_record = {
        'admission_number': admission_number,
        'name': name,
        'Percentage': Percentage
    }

    # Append the new record to the binary file
    with open("employee.dat", "ab") as file:  # Open file in append binary mode
        pickle.dump(student_record, file)

def count_rec():
    count = 0
    students_above_75 = []

    try:
        with open("student.dat", "rb") as file:  # Open file in read binary mode
            while True:
                try:
                    student = pickle.load(file)  # Deserialize the student object
                    if student.percentage > 75:  # Check if percentage is above 75
                        students_above_75.append(student)
                        count += 1
                except EOFError:
                    break  # End of file reached
    except FileNotFoundError:
        print("The file 'student.dat' does not exist.")
        return

    # Display the details of students scoring above 75%
    print(f"\nStudents scoring above 75%:\n")
    for student in students_above_75:
        print(f"Admission Number: {student.admission_number}, Name: {student.name}, Percentage: {student.percentage}")

    print(f"\nTotal number of students scoring above 75%: {count}")

# add_student_record()
# count_rec

# Given a binary file employee.dat, created using dictionary object having keys:
# (empcode, name, and salary)
# -Write a python function that add one more record at the end of file.
# -Write a python function that display all employee records whose salary is more that 30000. 
def add_employee_record():
    empcode = input("Enter Employee Code: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))

    # Create a dictionary for the employee record
    employee_record = {
        'empcode': empcode,
        'name': name,
        'salary': salary
    }

    # Append the new record to the binary file
    with open("employee.dat", "ab") as file:  # Open file in append binary mode
        pickle.dump(employee_record, file)  # Serialize and write the employee dictionary to the file


def display_high_salary_employees():
    try:
        with open("employee.dat", "rb") as file:  # Open file in read binary mode
            print("\nEmployees with salary greater than 30,000:\n")
            count = 0

            while True:
                try:
                    employee = pickle.load(file)  # Deserialize the employee dictionary
                    if employee['salary'] > 30000:  # Check if salary is greater than 30,000
                        print(f"EmpCode: {employee['empcode']}, Name: {employee['name']}, Salary: {employee['salary']}")
                        count += 1
                except EOFError:
                    break  # End of file reached

            if count == 0:
                print("No employees found with salary greater than 30,000.")

    except FileNotFoundError:
        print("The file 'employee.dat' does not exist.")

# add_employee_record()
# display_high_salary_employees()

# 10- A binary file players.dat, containing records of following list format:
# [code, name, country and total runs]
# (i)-Write a python function that display all records where player name starts from 'A'
# (ii)-Write a python function that accept country as an argument and count
# and display the number of players of that country.
# (iii)-Write a python function that add one record at the end of file.

def count_players_by_country(country):
    count = 0
    try:
        with open("players.dat", "rb") as file:  # Open file in read binary mode
            while True:
                try:
                    player = pickle.load(file)  # Deserialize the player record
                    if player[2].lower() == country.lower():  # Check if country matches
                        count += 1
                except EOFError:
                    break  # End of file reached

        print(f"\nTotal number of players from {country}: {count}")

    except FileNotFoundError:
        print("The file 'players.dat' does not exist.")


def add_player_record():
    code = input("Enter Player Code: ")
    name = input("Enter Player Name: ")
    country = input("Enter Player Country: ")
    total_runs = int(input("Enter Total Runs: "))

    # Create a list for the player record
    player_record = [code, name, country, total_runs]

    # Append the new record to the binary file
    with open("players.dat", "ab") as file:  # Open file in append binary mode
        pickle.dump(player_record, file)

def display_players_starting_with_a():
    try:
        with open("players.dat", "rb") as file:  # Open file in read binary mode
            print("\nPlayers whose names start with 'A':\n")
            found = False

            while True:
                try:
                    player = pickle.load(file)  # Deserialize the player record
                    if player[1].startswith('A'):  # Check if name starts with 'A'
                        print(f"Code: {player[0]}, Name: {player[1]}, Country: {player[2]}, Total Runs: {player[3]}")
                        found = True
                except EOFError:
                    break  # End of file reached

            if not found:
                print("No players found whose names start with 'A'.")

    except FileNotFoundError:
        print("The file 'players.dat' does not exist.")

# add_player_record()
# count_players_by_country("India")
# display_players_starting_with_a()
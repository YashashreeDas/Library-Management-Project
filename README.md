Library Management System
Introduction

This project is a simple Library Management System made using Python. I developed it as a project for the Python Essentials course.

The main purpose of this project is to manage some common activities of a small library through a command-line application. Instead of keeping book and member information manually, the program stores the information using an SQLite database.

The application can be used to add and search for books, register members, issue books, return books, and check which books are currently issued.

The project is completely terminal-based, so it does not require a graphical interface to run.

Main Features

The application provides the following options:

Add Book

View Books

Search Book

Register Member

View Members

Issue Book

Return Book

View Issued Books

Exit

1. Add Book

A new book can be added by entering:

Book title

Author name

ISBN

Each book is automatically given a unique ID.

2. View Books

This option displays all books currently stored in the library.

It shows:

Book ID

Title

Author

ISBN

Availability status

The status shows whether a book is currently Available or Issued.

3. Search Book

Books can be searched using:

Title

Author

ISBN

This makes it easier to find a particular book.

4. Register Member

New library members can be registered by entering:

Member name

Email

Phone number

Each member receives a unique member ID.

5. View Members

This option displays registered members along with their:

Member ID

Name

Email

Phone number

6. Issue Book

A book can be issued to a registered member.

The program asks for:

Book ID

Member ID

Before issuing the book, the program checks whether the book exists, whether it is available, and whether the member exists.

The issue date and due date are stored in the database.

7. Return Book

When a member returns a book, the program records the return date.

It also checks whether the book is overdue. If it is returned after the due date, the program calculates a fine based on the number of overdue days.

8. View Issued Books

This option shows books that are currently issued.

It displays:

Book title

Member name

Issue date

Due date

9. Exit

This option closes the application.

Technologies Used

The project was made using:

Python

SQLite

Python is used for the application logic, user input, menu system, database operations, and date calculations.

SQLite is used to store the library data. It is suitable for this project because it does not require a separate database server.

Python Modules Used

The project uses Python's built-in modules:

sqlite3 - for working with the SQLite database

datetime - for issue dates, due dates, and overdue calculations

unittest - for basic testing

No external Python packages are required.

Project Structure
library_management/
│
├── main.py
├── database.py
├── books.py
├── members.py
├── transactions.py
├── test_library.py
├── README.md
├── requirements.txt
└── .gitignore

main.py

This is the main file of the application. It displays the menu and connects the different parts of the project.

database.py

This file handles the SQLite database connection and creates the required database tables.

The main tables are:

Books

Members

Transactions

books.py

This file contains functions related to books, such as adding, viewing, and searching for books.

members.py

This file contains functions for registering and viewing library members.

transactions.py

This file handles book issuing, book returns, due dates, and fine calculation.

test_library.py

This file contains a basic test for the project.

requirements.txt

This file documents the project's dependency status. No external packages are required.

library.db

The SQLite database file is created automatically when the program is run for the first time.

It does not need to be created manually.

The local database file is excluded from GitHub using .gitignore.

Requirements

Before running the project, make sure you have:

Python 3.x

PowerShell, Command Prompt, or another terminal

The project files downloaded or cloned from the repository

No separate SQLite installation is required because SQLite support is included with Python.

Environment Setup
Step 1: Check Python

Open a terminal and check whether Python is installed:

python --version


A Python 3 version should be displayed.

If python is not recognized on your system, try:

python3 --version

Step 2: Open the Project Folder

Open the terminal and move into the project folder.

For example:

cd library_management


The exact location of the folder can be different depending on where the project was downloaded.

Step 3: Create a Virtual Environment (Optional)

A virtual environment can be created to keep the project environment separate:

python -m venv venv


On Windows PowerShell, activate it using:

.\venv\Scripts\Activate.ps1


On Windows Command Prompt:

venv\Scripts\activate


A virtual environment is optional for this project because the application uses only Python's built-in modules.

Step 4: Install Dependencies

No external Python packages are required.

The project uses Python's standard library modules such as:

sqlite3

datetime

unittest

Therefore, no pip install command is required.

Step 5: Run the Application

From inside the project folder, run:

python main.py


If your system uses python3, run:

python3 main.py


The Library Management System menu will then appear in the terminal.

Step 6: Database Setup

No manual database setup is required.

When the application is run for the first time, it automatically creates an SQLite database named:

library.db


The database contains tables for:

Books

Members

Book issue and return transactions

The database is created locally and does not need to be downloaded separately.

Step 7: Run the Tests

The project includes a basic unit test.

Run:

python -m unittest test_library.py


If your system uses python3:

python3 -m unittest test_library.py


A successful test run should display:

OK

Using the Application

When the program starts, the following menu is displayed:

=============================================
       LIBRARY MANAGEMENT SYSTEM
=============================================
1. Add Book
2. View Books
3. Search Book
4. Register Member
5. View Members
6. Issue Book
7. Return Book
8. View Issued Books
9. Exit
=============================================
Enter your choice:


Enter the number of the operation you want to perform.

Example Workflow

A normal use of the application can be:

Add one or more books.

Register a library member.

View the books to find the Book ID.

View the members to find the Member ID.

Issue an available book to the member.

View the issued books.

Return the book.

Check the fine if the book was returned late.

Database Design

The application uses three tables.

Books Table

The books table stores information about books.

It contains:

ID

Title

Author

ISBN

Availability

Members Table

The members table stores information about registered members.

It contains:

ID

Name

Email

Phone

Transactions Table

The transactions table stores information about book issues and returns.

It contains:

Transaction ID

Book ID

Member ID

Issue date

Due date

Return date

This allows the program to keep track of which member has a particular book.

Overdue Fine

The default loan period in the project is 7 days.

If a book is returned after its due date, the program calculates the number of overdue days.

The fine rate used by the application is:

₹5 per overdue day


For example, if a book is returned 3 days late:

3 × ₹5 = ₹15


If the book is returned on or before the due date:

₹0

Error Handling

The program includes checks for common situations, including:

Invalid menu choices

Invalid numeric IDs

Book ID that does not exist

Member ID that does not exist

Trying to issue an already issued book

Trying to return a book that is not currently issued

Duplicate ISBN

Duplicate member email

These checks help prevent incorrect information from being entered into the database.

Testing

I tested the application through the command line.

The main operations tested were:

Adding a book

Viewing books

Searching for a book

Registering a member

Viewing members

Issuing a book

Viewing issued books

Returning a book

Exiting the application

I also ran the basic unit test included in test_library.py.

Future Improvements

Some features that could be added in the future are:

Admin login

Editing book details

Removing books

Editing member information

Removing members

Support for multiple copies of the same book

More detailed library reports

Better search and filtering

Graphical user interface

Conclusion

This project helped me practice Python concepts such as functions, modules, database operations, user input, conditional statements, exception handling, and date handling.

It also gave me experience in connecting a Python program with an SQLite database and building a complete application that can be used from the command line.

Author

Yashashree Das
Registration No.: 26BAI10240

Python Essentials Course Project
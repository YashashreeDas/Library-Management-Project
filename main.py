from database import initialize_database
from books import add_book, view_books, search_books
from members import add_member, view_members
from transactions import (
    issue_book,
    return_book,
    view_issued_books
)


def display_menu():
    print("\n" + "=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Register Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View Issued Books")
    print("9. Exit")
    print("=" * 45)


def main():
    initialize_database()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()

            if title and author and isbn:
                add_book(title, author, isbn)
            else:
                print("All fields are required.")

        elif choice == "2":
            view_books()

        elif choice == "3":
            keyword = input("Enter title, author, or ISBN: ").strip()

            if keyword:
                search_books(keyword)
            else:
                print("Search keyword cannot be empty.")

        elif choice == "4":
            name = input("Enter member name: ").strip()
            email = input("Enter email: ").strip()
            phone = input("Enter phone number: ").strip()

            if name and email and phone:
                add_member(name, email, phone)
            else:
                print("All fields are required.")

        elif choice == "5":
            view_members()

        elif choice == "6":
            try:
                book_id = int(input("Enter book ID: "))
                member_id = int(input("Enter member ID: "))
                issue_book(book_id, member_id)

            except ValueError:
                print("Please enter valid numeric IDs.")

        elif choice == "7":
            try:
                book_id = int(input("Enter book ID: "))
                return_book(book_id)

            except ValueError:
                print("Please enter a valid book ID.")

        elif choice == "8":
            view_issued_books()

        elif choice == "9":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

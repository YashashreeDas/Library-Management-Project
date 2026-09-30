from datetime import date, timedelta
from database import get_connection


LOAN_DAYS = 7
FINE_PER_DAY = 5


def issue_book(book_id, member_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT available FROM books WHERE id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book not found.")
        connection.close()
        return

    if book[0] == 0:
        print("Book is already issued.")
        connection.close()
        return

    cursor.execute(
        "SELECT id FROM members WHERE id = ?",
        (member_id,)
    )

    member = cursor.fetchone()

    if member is None:
        print("Member not found.")
        connection.close()
        return

    issue_date = date.today()
    due_date = issue_date + timedelta(days=LOAN_DAYS)

    cursor.execute(
        """
        INSERT INTO transactions
        (book_id, member_id, issue_date, due_date)
        VALUES (?, ?, ?, ?)
        """,
        (
            book_id,
            member_id,
            issue_date.isoformat(),
            due_date.isoformat()
        )
    )

    cursor.execute(
        "UPDATE books SET available = 0 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Book issued successfully.")
    print(f"Due date: {due_date}")


def return_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, due_date
        FROM transactions
        WHERE book_id = ?
        AND return_date IS NULL
        """,
        (book_id,)
    )

    transaction = cursor.fetchone()

    if transaction is None:
        print("This book is not currently issued.")
        connection.close()
        return

    transaction_id = transaction[0]
    due_date = date.fromisoformat(transaction[1])
    return_date = date.today()

    overdue_days = max(
        0,
        (return_date - due_date).days
    )

    fine = overdue_days * FINE_PER_DAY

    cursor.execute(
        """
        UPDATE transactions
        SET return_date = ?
        WHERE id = ?
        """,
        (return_date.isoformat(), transaction_id)
    )

    cursor.execute(
        "UPDATE books SET available = 1 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    print("Book returned successfully.")
    print(f"Overdue days: {overdue_days}")
    print(f"Fine: ₹{fine}")


def view_issued_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            books.title,
            members.name,
            transactions.issue_date,
            transactions.due_date
        FROM transactions
        JOIN books
            ON transactions.book_id = books.id
        JOIN members
            ON transactions.member_id = members.id
        WHERE transactions.return_date IS NULL
        """
    )

    records = cursor.fetchall()
    connection.close()

    if not records:
        print("No books are currently issued.")
        return

    print("\nIssued Books")
    print("-" * 70)

    for record in records:
        print(f"Book: {record[0]}")
        print(f"Member: {record[1]}")
        print(f"Issue Date: {record[2]}")
        print(f"Due Date: {record[3]}")
        print("-" * 70)

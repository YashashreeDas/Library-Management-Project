from database import get_connection


def add_book(title, author, isbn):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO books (title, author, isbn)
            VALUES (?, ?, ?)
            """,
            (title, author, isbn)
        )

        connection.commit()
        print("Book added successfully.")

    except Exception as error:
        print(f"Could not add book: {error}")

    finally:
        connection.close()


def view_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, author, isbn, available FROM books"
    )

    books = cursor.fetchall()
    connection.close()

    if not books:
        print("No books found.")
        return

    print("\nID | Title | Author | ISBN | Status")
    print("-" * 70)

    for book in books:
        status = "Available" if book[4] else "Issued"

        print(
            f"{book[0]} | {book[1]} | {book[2]} | "
            f"{book[3]} | {status}"
        )


def search_books(keyword):
    connection = get_connection()
    cursor = connection.cursor()

    search_term = f"%{keyword}%"

    cursor.execute(
        """
        SELECT id, title, author, isbn, available
        FROM books
        WHERE title LIKE ?
           OR author LIKE ?
           OR isbn LIKE ?
        """,
        (search_term, search_term, search_term)
    )

    books = cursor.fetchall()
    connection.close()

    if not books:
        print("No matching books found.")
        return

    for book in books:
        status = "Available" if book[4] else "Issued"

        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"ISBN: {book[3]} | "
            f"Status: {status}"
        )

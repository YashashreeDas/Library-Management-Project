from database import get_connection


def add_member(name, email, phone):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO members (name, email, phone)
            VALUES (?, ?, ?)
            """,
            (name, email, phone)
        )

        connection.commit()
        print("Member registered successfully.")

    except Exception as error:
        print(f"Could not register member: {error}")

    finally:
        connection.close()


def view_members():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, email, phone FROM members"
    )

    members = cursor.fetchall()
    connection.close()

    if not members:
        print("No members found.")
        return

    print("\nID | Name | Email | Phone")
    print("-" * 60)

    for member in members:
        print(
            f"{member[0]} | {member[1]} | "
            f"{member[2]} | {member[3]}"
        )

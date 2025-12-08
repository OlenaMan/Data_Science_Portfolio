'''
shelf_track: an application for managing a bookstore's inventory.

Features:

- Create and initialise an SQLite database (ebookstore.db)with 'book' and 'author' tables.
- Add, update, delete, and search books.
- View details of all books (title, offer, name, country) via INNER JOIN.
- Update the linked author's name  and country from a selected book.
- Input validation (4-digit numeric IDs)
- Parameterized queries and error handling.
'''

import sqlite3


def get_conn():
    '''
    Return a SQLite connection with forfeign keys enforced.
    '''
    conn = sqlite3.connect('ebookstore.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enforce foreign key constraints
    return conn


def init_db():
    '''Create required tables and insert initial data if not present.'''
    with get_conn() as conn:
        c = conn.cursor()

        # Create and populate tables: author and book
        c.execute('''CREATE TABLE IF NOT EXISTS author(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT NOT NULL
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            authorID INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            FOREIGN KEY(authorID) REFERENCES author(id)
        )''')
        # insert rows in 'autor' table
        authors = [
            (1290, "Charles Dickens", "England"),
            (8937, "J.K. Rowling", "England"),
            (2356, "C.S. Lewis", "Ireland"),
            (6380, "J.R.R. Tolkien", "South Africa"),
            (5620, "Lewis Carroll", "England")
            ]
        c.executemany('''
        INSERT OR IGNORE INTO author(id, name, country)
        VALUES (?, ?, ?)''', authors)

        # insert rows in 'book' table
        books = [
            (3001, "A Tale of Two Cities", 1290, 30),
            (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
            (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice's Adventures in Wonderland", 5620, 12)
        ]
        c.executemany('''INSERT OR IGNORE INTO book(
                        id, title, authorID, qty)
                        VALUES(?,?,?,?)''', books)


def get_int_input(prompt, length=None):
    '''
    Prompt for an integer, with a fixed digit length.
    '''

    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("Enter digits only.")
            continue
        if length and len(value) != length:
            print("Please enter exactly {length} digits.")
            continue
        return int(value)


def author_exists(conn, author_id):
    '''
    Return True if an author with the given id exists.
    '''
    c = conn.execute('''SELECT 1 from author WHERE id = ?''', (author_id,))
    return c.fetchone() is not None


def book_exists(conn, book_id):
    '''
    Return True if a book with a given id exists.
    '''
    c = conn.execute(''' SELECT 1 from book WHERE id = ?''', (book_id,))
    return c.fetchone() is not None


def ensure_author(conn, author_id):
    '''
    Ensure the author id exists, if not, offer to create it interactively.
    '''
    if author_exists(conn, author_id):
        return True
    print("Author ID not found")
    offer = input("Add this author now? (y/n):").strip().lower()
    if offer == "y":
        name = input("Author name: ").strip()
        country = input("Author country: ").strip()
        try:
            conn.execute('''
                INSERT INTO author(id, name, country)
                VALUES (?, ?, ?)''', (author_id, name, country))
            conn.commit()
            print("Author added.")
            return True
        except sqlite3.IntegrityError as e:
            print(f"Failed to add author: {e}")
            return False


def enter_book(conn):
    '''
    Create a new book after validating IDs and quantity.
    '''
    book_id = get_int_input("Book ID (4 digits): ", length=4)
    book_title = input("Book title: ").strip()
    qty = get_int_input("Book quantity: ")
    author_id = get_int_input("Book author ID (4 digits): ", length=4)

    if not ensure_author(conn, author_id):
        return
    try:
        conn.execute('''
            INSERT INTO book (id, title, authorID, qty)
            VALUES (?, ?, ?, ?)''', (book_id, book_title, author_id, qty))
        conn.commit()
        print("Book added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Insert failed: {e}")


def update_book(conn):
    '''Update a book. Default is to update quantity, but user can choose:
    1. qty, 2. title, 3. authorID, or 4. linked author's name and/or country.
    '''
    book_id = get_int_input("Book ID to update: ")
    if not book_exists(conn, book_id):
        print("Book not found.")
        return

    # default is quantity but let user choose
    print("Update options:\n 1. Quantity\n 2. Title\n 3. AuthorID\n "
        "4. Author name/country")
    choice = input("Choose the option number: ").strip()
    try:
        if choice == "1":
            new_qty = get_int_input("New quantity: ")
            conn.execute('''
                UPDATE book SET qty = ? WHERE id = ? ''',
                (new_qty, book_id))
            conn.commit()
            print("Quantity added.")
        elif choice == "2":
            new_title = input("Enter new book title: ").strip()
            conn.execute('''
                UPDATE book SET title = ? WHERE id = ?''',
                (new_title, book_id))
            conn.commit()
            print("Title updated.")
        elif choice == "3":
            new_a_id = get_int_input("New author ID (4 digits): ", length=4)
            if not ensure_author(conn, new_a_id):
                return
            conn.execute('''
                UPDATE book SET authorID = ? WHERE id = ?''',
                (new_a_id, book_id))
            conn.commit()
            print("Author ID updated.")
        elif choice == "4":
            # show current author details (INNER JOIN)
            # and let update name/country
            row = conn.execute(''' SELECT a.id, a.name, a.country
                        FROM book b INNER JOIN author a ON b.authorID = a.id
                        WHERE b.id = ?''', (book_id,)).fetchone()
            if not row:
                print("Author not found.")
                return
            aid, aname, acountry = row
            print(f"Current author ID: {aid}, Name: {aname}, Country: {acountry}")

            new_name = input("New author name (blank to keep):  ").strip()
            new_country = input(" New author country (blank to keep): ").strip()
            if not new_name or new_country:
                print("No changes made.")
                return

            if new_name and new_country:
                conn.execute('''
                    UPDATE author SET name = ?, country = ?
                    WHERE id = ?''', (new_name, new_country, aid))
            elif new_name:
                conn.execute('''
                    UPDATE author SET name = ? WHERE id = ?''', (new_name, aid))
            else:
                conn.execute('''
                    UPDATE author SET country = ? WHERE id = ?''', (new_country, aid))
            conn.commit()
            print("Author details updated successfully.")
        else:
            print("invalid option.")
    except sqlite3.IntegrityError as e:
        print(f"Update failed: {e}")


def delete_book(conn):
    '''Delete a book by ID.'''
    book_id = get_int_input("Book ID to delete (4 digits): ", length=4)
    if not book_exists(conn, book_id):
        print("Book not found.")
        return
    conn.execute('''DELETE FROM book WHERE id = ?''', (book_id,))
    conn.commit()
    print("Book deleted.")


def search_books(conn):
    '''Search for books by case-incensitive title keyword.'''
    search_book = input(" Search by title keyword: ").strip()
    c = conn.execute('''
            SELECT id, title, authorID, qty FROM book WHERE LOWER(title) LIKE ?
            ''', (f"%{search_book.lower()}%",))
    rows = c.fetchall()
    if not rows:
        print("No matches found.")
        return
    for r in rows:
        print(f"{r[0]} | {r[1]} | authorID={r[2]} | qty={r[3]}")


def view_all_books(conn):
    '''Display all books with author name and country using an INNER JOIN.'''
    c = conn.execute('''
            SELECT b.title AS Title, a.name AS AuthorName, a.country AS Country
            FROM book b
            INNER JOIN author a ON b.authorID = a.id
            ORDER by b.title''')
    rows = c.fetchall()
    if not rows:
        print("No books found.")
        return
    print("\nDetails")
    print("-" * 50)
    for title, author, country in rows:
        print(f"Title: {title}\nAuthor's Name: {author}\nAuthor's Country: {country}")
        print("-" * 50)


def main():
    ''' Initialise the databse and tun the interactive menu.'''
    init_db()
    with get_conn() as conn:
        while True:
            choice = input(
                        ''' Select one of the following options (as a number):
                        1 - Enter book
                        2 - Update book
                        3 - Delete book
                        4 - Search books
                        5 - View details of all books
                        0 - Exit
                    ''').strip()
            if choice == "1":
                enter_book(conn)
            elif choice == "2":
                update_book(conn)
            elif choice == "3":
                delete_book(conn)
            elif choice == "4":
                search_books(conn)
            elif choice == "5":
                view_all_books(conn)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

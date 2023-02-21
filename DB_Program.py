import sqlite3


# Class creates/opens sqlite database and creates cursor
class BookDatabase:
    # Initializes attributes of the class, takes the name of the database as an argument.
    def __init__(self, database):
        self.con = sqlite3.Connection(database)
        self.cur = self.con.cursor()


# Class creates a book object by taking the below attributes
class Book:
    def __init__(self, id=int, title=str, author=str, qty=int):
        self.id = id
        self.title = title
        self.auther = author
        self.qty = qty

    # Class function outputs attributes as a list
    def group(self):
        return [self.id, self.title, self.auther, self.qty]


# Creates database using 'BookDatabase' class
db = BookDatabase('Book_db')
# Uses cursor execute a query that creates a tabel called book_tale with the
db.cur.execute("""CREATE TABLE IF NOT EXISTS book_table(id INTEGER PRIMARY KEY, title TEXT, author TEXT,
       quantity INTEGER)""")


# Function takes the attributes and  creates a book object with is inserted into table
def enter_book():
    try:
        print("Add Book")
        book_id = int(input("Enter book id number :"))
        book_title = input("Enter book title :")
        book_author = input("Enter author of book :")
        book_quantity = int(input("Enter book quantity number :"))
        new_book = Book(book_id, book_title, book_author, book_quantity)
        db.cur.execute('''INSERT INTO book_table 
            VALUES(?,?,?,?)''', new_book.group())
        db.con.commit()
    except ValueError:
        print("input error")


""" Function displays all entry's then prompts user to enter the id num to select a book. User is then prompted to enter
a number to update the book quantity 
"""


def update_book():
    # Try block prevents crash if user enter the wrong data type
    try:
        print("Table of Contents - Update")
        db.cur.execute("SELECT * FROM book_table WHERE id>0")
        print(db.cur.fetchall())
        book_selector = input("Enter the id number to select a book :")
        new_quantity = int(input("Update quantity :"))
        db.cur.execute("""UPDATE book_table
                    SET quantity=?
                    WHERE id=?""", (new_quantity, book_selector))
        db.con.commit()
    except ValueError:
        print("input error")


# Displays all entry's, prompts user enter id of book they want deleted. This book is then deleted from the table.
def delete_book():
    try:
        print("Table of Contents - Delete")
        db.cur.execute("SELECT * FROM book_table WHERE id>0")
        print(db.cur.fetchall())
        del_book = int(input("Enter id to delete book :"))
        db.cur.execute("""DELETE FROM book_table
                    WHERE id=?
                    """, (del_book,))
        db.con.commit()
    except ValueError:
        print("input error")


# Prompts user to input the id, title or author to search for the book.
def search_book():
    print("Book Search")
    search_input = input("Search for book using 'id', 'title' or 'author' :")
    db.cur.execute('SELECT * FROM book_table WHERE id=?', (search_input,))
    print(db.cur.fetchall())
    db.cur.execute('SELECT * FROM book_table WHERE title=?', (search_input,))
    print(db.cur.fetchall())
    db.cur.execute('SELECT * FROM book_table WHERE author=?', (search_input,))
    print(db.cur.fetchall())


# Creates a menu
while True:
    menu_operator = input("ADD new book to database - 1 \n"
                          "UPDATE book information - 2\n"
                          "DELETE books from the database -3\n"
                          "SEARCH the database to find a specific book - 4\n"
                          "EXIT = 0\n"
                          ":")
    if menu_operator == "1":
        enter_book()

    elif menu_operator == "2":
        update_book()

    elif menu_operator == "3":
        delete_book()

    elif menu_operator == "4":
        search_book()
    elif menu_operator == "0":
        exit()
    else:
        print("invalid menu input")
        pass

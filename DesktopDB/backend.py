import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (_id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows 

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * from book WHERE title = ? OR author = ? OR year = ? or isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE _id = ?", (id,))
    conn.commit()
    conn.close()

def update(title, author, year, isbn, id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE _id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert("The Earth", "John Smith", 1918, 123666789)
#print(search(author = "John Smith"))
#delete(2)
update("Jupiter", "John Smith", 1918, 123666789, 1)
print(view())
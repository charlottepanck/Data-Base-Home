import sqlite3

# functions


def fetch_author_id():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Author;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Author ID | Author's Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")
    db.close


def fetch_all_series():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Series;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Series ID | Series Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")


def fetch_all_books():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Title FROM Books ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        titlelength = len(x)
        spaces = (titlelength-5) * " "

    sql2 = "SELECT name FROM author ORDER BY Length(name) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        authorlength = len(x)
        authorspaces = (authorlength-6) * " "

    sql3 = "SELECT series_title FROM series ORDER BY Length(series_title) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        serieslength = len(x)
        seriesspaces = (serieslength-6) * " "

    sql = """SELECT Books.book_id, Books.Title, Author.name, Series.series_title, Books.availability
FROM Books
LEFT JOIN Author ON Books.Author = Author.id
LEFT JOIN Series ON Books.series = series.id;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {spaces}| Author {authorspaces}| Series {seriesspaces}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{titlelength}} | {i[2]:{authorlength}} | {i[3]:{serieslength}} | {i[4]}")
    db.close()


def fetch_all_members():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-8) * " "

    sql2 = "SELECT Surname FROM Members ORDER BY Length(surname) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        surnamelength = len(x)
        surnamespaces = (surnamelength-7) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Forename {forenamespaces}| Surname {surnamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{surnamelength}} | {i[3]:{emaillength}} | {i[4]}")
    db.close()


def fetch_panckhurst():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-8) * " "
    sql2 = "SELECT Surname FROM Members ORDER BY Length(surname) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        surnamelength = len(x)
        surnamespaces = (surnamelength-7) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Surname = 'Panckhurst';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Forename {forenamespaces}| Surname {surnamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{surnamelength}} | {i[3]:{emaillength}} | {i[4]}")
    db.close()


def fetch_all_minors():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-8) * " "

    sql2 = "SELECT Surname FROM Members ORDER BY Length(surname) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        surnamelength = len(x)
        surnamespaces = (surnamelength-7) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Age < 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Forename {forenamespaces}| Surname {surnamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{surnamelength}} | {i[3]:{emaillength}} | {i[4]}")
    db.close()


def fetch_all_adults():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-8) * " "

    sql2 = "SELECT Surname FROM Members ORDER BY Length(surname) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        surnamelength = len(x)
        surnamespaces = (surnamelength-7) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Age >= 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"MemberID | Forename {forenamespaces}| Surname {surnamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[1]:<8} | {i[1]:<{forenamelength}} | {i[2]:{surnamelength}} | {i[3]:{emaillength}} | {i[4]}")
    db.close()


# main code
print("""Welcome to Libaray Database
Enter 1 to view all books --> view specific book with more deatils --> view
Enter 2 to view all members --> view who has books out -->
Enter 3 to view
Enter 4 to view
Enter "stop" to exit program""")
while True:
    userinput = input('>> ').lower()
    if userinput == '1':
        fetch_all_books()
    elif userinput == '2':
        fetch_all_members()

import sqlite3


def fetch_author_id():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Author;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Author ID  | Author's Name")
    for i in results:
        print(f"{i[0]:10} | {i[1]}")
    db.close


def fetch_all_books():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Book ID | Title                         | Author")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:<29} | {i[2]:}")
    db.close()


def fetch_all_members():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Members;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("MemberID | Foreame   | Surname         | Contact Info            | Age")
    for i in results:
        print(f"{i[0]:>8} | {i[1]:<9} | {i[2]:15} | {i[3]:23} | {i[4]}")
    db.close()


def fetch_panckhurst():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Members WHERE Surname = 'Panckhurst';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("MemberID | Forename  | Surname    | Contact Info            | Age")
    for i in results:
        print(f"{i[0]:>8} | {i[1]:<9} | {i[2]:10} | {i[3]:23} | {i[4]}")
    db.close()


def fetch_all_minors():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()    
    sql = "SELECT * FROM Members WHERE Age < 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("MemberID | Foreame   | Surname         | Contact Info            | Age")
    for i in results:
        print(f"{i[0]:>8} | {i[1]:<9} | {i[2]:15} | {i[3]:23} | {i[4]}")
    db.close()


def fetch_all_adults():
    db = sqlite3.connect('Pratice.db')
    cursor = db.cursor()    
    sql = "SELECT * FROM Members WHERE Age >= 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("MemberID | Forename  | Surname    | Contact Info           | Age")
    for i in results:
        print(f"{i[0]:>8} | {i[1]:<9} | {i[2]:10} | {i[3]:22} | {i[4]}")
    db.close()

#   fetch_panckhurst()
#   fetch_all_books()
#   fetch_all_minors()
#   fetch_all_members()
#   fetch_author_id()
#   fetch_all_adults()
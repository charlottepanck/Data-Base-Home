import sqlite3


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
    sql = "SELECT * FROM Books;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {spaces}| Author | Series")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:<{titlelength}} | {i[2]:<6} | {i[3]}")
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

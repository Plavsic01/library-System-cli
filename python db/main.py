import db_connection

db = db_connection.connect_db("localhost", "root", "najbolji3", "userDB")
db_cursor = db.cursor()
print()


# ADMIN LOGIN
# IF LOGIN == SUCCESS SHOW ADMIN MENU 
def adminMenu():
    db_list = []

    print("Login to admin account")
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))

    sql_code = "SELECT * FROM register_admin WHERE username = '{}'AND password = {}".format(username,password)

    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        db_list.append(data_list)
    
    

    for i in range(len(db_list)):
        if(username in db_list[i] and password in db_list[i]):
            print("Welcome {}\nYou are logged in as ADMIN.\n".format(username.capitalize()))
            choose_admin_options()
            break

  

    if(len(db_list)==0):
        print("There is no admin in database!")

# CHOOSE WHAT YOU WANT TO DO WITH ADMIN PRIVILEGES
def choose_admin_options():
    print("Choose action: \n1.Add librarian\n2.View librarian\n3.Delete librarian\n4.Exit\n")
    action = int(input("Choose: "))
    if(action == 1):
        add_librarian()
    elif(action == 2):
        view_librarian()
    elif(action == 3):
        delete_librarian()
    elif(action==4):
        exit(0)
    else:
        choose_admin_options()
   
# DELETE LIBRARIAN AS ADMIN
def delete_librarian():
    try:
        view_lib = view_librarian()
        print("Which librarian you want to delete? ")
        num = int(input("Choose number: "))

        sql_code = "DELETE FROM register_librarian WHERE idregister_librarian = {}".format(num)
        db_cursor.execute(sql_code)
        db.commit()
        print("Successfully deleted librarian from the database.")

    except:
        print("Error Accured...")
        print("Going back to main menu...\n")
        mainMenu()


# ADD LIBRARIAN AS ADMIN
def add_librarian():
    try:
        username = input("Enter librarian username: ")
        password = int(input("Enter librarian password: "))
        sql_code = "INSERT INTO register_librarian (username,password) VALUES ('{}',{})".format(username,password)

        db_cursor.execute(sql_code)
        db.commit()

        print("Librarian added.")

    except:
        print("Failed to add librarian...")
    

# VIEW ALL LIBRARIANS AS ADMIN
def view_librarian():

    list_of_librarians = []

    sql_code = "SELECT * FROM register_librarian"
    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        list_of_librarians.append(data_list)

    for i in range(len(list_of_librarians)):
        print("{}. username = {}, password = {}".format(list_of_librarians[i][0],list_of_librarians[i][1],list_of_librarians[i][2]))
    return list_of_librarians

# REGISTER ADMIN IN DATABASE
def registerAdmin():
    print("Welcome to register admin page.\nEnter your username and password.")
    username = input("your username: ")
    password = input("your password **MUST BE ATLEAST 5 NUMBERS**: ")
    lenPassword = 5


    vec_postoji = []

    sql_code = "SELECT * FROM register_admin WHERE username = '{}'AND password = {}".format(username,password)
    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        vec_postoji.append(data_list)
        

    if(len(vec_postoji) == 0):
        sql_code = "INSERT INTO register_admin (username,password) VALUES ('{}',{})".format(username,password)

        if(len(password) >= lenPassword):
            password = int(password)
            db_cursor.execute(sql_code)
            db.commit()
        else:
            print("Password is too weak. Try again!\n")
            mainMenu()
    else:
        print("Admin already exists.\nTry again.\n")
        mainMenu()



# LIBRARIAN LOGIN MENU
def login_librarian():

    db_list = []
    

    print("Login to librarian account")
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))

    sql_code = "SELECT * FROM register_librarian WHERE username = '{}'AND password = {}".format(username,password)

    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        db_list.append(data_list)
    

    for i in range(len(db_list)):
        if(username in db_list[i] and password in db_list[i]):
            print("Welcome {}\nYou are logged in as LIBRARIAN.\n".format(username.capitalize()))
            choose_librarian_options()
            break


    if(len(db_list)==0):
        print("There is no librarian in database!")


def choose_librarian_options():
    print("1.Add books\n2.Issue books\n3.View issued books\n4.Return books\n5.Exit\n")
    action = int(input("Choose option: "))
    if(action == 1):
        add_books()
    elif(action == 2):
        issue_books()
    elif(action == 3):
        view_issued_books()
    elif(action==4):
        return_books()
    elif(action == 5):
        exit(0)
    else:
        choose_librarian_options()



# ADD BOOKS AS LIBRARIAN
def add_books():
    try:
        print("ADD BOOKS: ")
        book_name = input("Enter book name: \n")
        author = input("Enter book's author: \n")
        sql_code = "INSERT INTO books (bookName,bookAuthor) VALUES ('{}','{}')".format(book_name,author)
        db_cursor.execute(sql_code)
        db.commit()
        print("Book added successfully!")
    except:
        print("Adding book failed...")

# ISSUE BOOKS
def issue_books():
    db_list = []
    exists = False

    print("ISSUE A BOOK: ")
    book_name = input("Enter book name: \n")
    author = input("Enter book's author: \n")

    sql_code = "SELECT * FROM books WHERE bookName = '{}'AND bookAuthor = '{}'".format(book_name,author)

    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        db_list.append(data_list)

    for i in range(len(db_list)):
        if(book_name == db_list[i][1] and author == db_list[i][2]):
            print(str(db_list[0][0]) + " " + str(db_list[0][1]) + " " + str(db_list[0][2]) + "\nBook is issued.")
            sql_code = "INSERT INTO issuedBooks (issuedBookName,issuedBookAuthor) VALUES ('{}','{}')".format(book_name,author)
            db_cursor.execute(sql_code)
            db.commit()
            exists = True
            break
    if(exists == False):
        print("There is no book with that name and author")


# VIEW ISSUED BOOKS AS LIBRARIAN
def view_issued_books():
    list_of_issued_books = []

    sql_code = "SELECT * FROM issuedBooks"
    db_cursor.execute(sql_code)
    result = db_cursor.fetchall()

    for res in result:
        data_list = list(res)
        list_of_issued_books.append(data_list)

    for i in range(len(list_of_issued_books)):
        print("{}. Book name = {}, book author = {}".format(list_of_issued_books[i][0],list_of_issued_books[i][1],list_of_issued_books[i][2]))
    return list_of_issued_books


# RETURN ISSUED BOOKS AS LIBRARIAN
def return_books():
    try:
        list_of_issued_books = []

        view_issued_books()

        print("which book do you want to return?")
        num = int(input("Enter number of the book you want to return: "))

        

        sql_code = "DELETE FROM issuedBooks WHERE idissuedBooks = {}".format(num)
        db_cursor.execute(sql_code)
        db.commit()
        print("Successfully returned book from the customer.")

    except:
        print("Failed to return book from the customer...")


def mainMenu():
    print("1.Register admin\n2.Login as librarian")
    print("3.Login as admin\n")


    choiceInput = int(input("Choose option: "))

    if(choiceInput == 1):
        registerAdmin()
    elif(choiceInput == 2):
        login_librarian()
    elif(choiceInput == 3):
        adminMenu() #admin login
    else:
        print("wrong choise!\nTry again!\n")
        mainMenu()

mainMenu()


# TODO
# 2. LIBRARIAN MENU 
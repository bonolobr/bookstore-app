#===== Import Libraries ===========

import sqlite3

from tabulate import tabulate

#===== Connect to Database ===========

# Connect to database and create cursor object
database = sqlite3.connect('ebookstore.db')
cursor = database.cursor()

#===== Define Functions ===========

def create_database():
    '''Creates a database called ebookstore and a table called books.'''


    book_details = [(3001, "A Tale of Two Cities", "Charles Dickens", 30), (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40), 
                    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25), (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), 
                    (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

    # Create table named books
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (id integer PRIMARY KEY, Title varchar(255), Author varchar(255), Qty integer)''')
    database.commit()

    #Insert book details into the books database table
    cursor.executemany('''INSERT OR IGNORE INTO books(id, Title, Author, Qty) VALUES (?,?,?,?)''', book_details)
    database.commit()


def display_full_book_database():
    '''Print out the full database on the screen.'''

    cursor.execute('''SELECT * FROM books ''')
    book_table = cursor.fetchall()
    print (tabulate(book_table, headers = ("id", "Title", "Author", "Qty"), tablefmt="fancy_grid"))


def display_selected_book_in_database(id):
    '''Print out the selected book in the ebookstore database on the screen.
      
        Parameter:
            id (int): Book id

        Returns:
            Book selected in table or indicates if book is not found.
    '''
   
   # Select book based on the id
    cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (id,))
    book_selected = cursor.fetchone()
        
    # If no book can be found with the selected id, print and return that the book is not found    
    if book_selected == None:
        print("Book not found in ebookstore database.")
        return "Book not found"

    # Else, print out the selected book in a table
    else:
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (id,))
        book_table = cursor.fetchall()
        print (tabulate(book_table, headers = ("id", "Title", "Author", "Qty"), tablefmt="fancy_grid"))

def enter_book():
    '''Enables user to add new books to the book table in the ebookstore database'''

    # Note leave id to autoincrement as the primary key and so no need for user to manually enter an id
    # Request user to enter the other book details (title, author & quantity) and add book to database once complete
    # Display error messages for invalid inputs for the quantity of books
    add_book_title = input("Enter the book title: ")
    add_book_author = input("Enter book author: ")
    while True:
        try: 
            add_book_quantity = int(input("Enter the quantity of books: "))
            if  add_book_quantity >= 0:
                break
            else:
                print("Error: Invalid input. Please enter an integer quantity number that is not a negative number.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer number for the quantity of books.")

    # Update the database with the new book 
    cursor.execute('''INSERT INTO books (Title, Author, Qty) VALUES (?,?,?)''', (add_book_title, add_book_author,add_book_quantity))
    database.commit()

    # Print out the final result
    print ("The new book has been successfully added to the database as follows: ")
    display_full_book_database()


def update_book(id):
    '''
    Enables user to update details for an existing book in the ebookstore database.
    
    Parameter:
        id (int): Book id

    Returns:
        Updated book in the book database table
    '''

    # Print out the database on the screen to show the books available for an update
    print ("The following are the books in the ebookstore database:")
    display_full_book_database()

    # Request user to enter the book id of the book details they would like to update
    while True:
        try:
            id = int(input("Please enter the id of the book whose information you would like to update from the table above: "))
            break
        except ValueError:
            print("Error: Invalid input for id. Please enter an integer number for the book id")

    if display_selected_book_in_database(id) != "Book not found":

        # Request user if they would like to update the title of the book selected. If yes, request user to update the title and update the database.
        choice_update_title = input("Would you like to update the book title (yes/no)? ")

        if choice_update_title.lower() == "yes":

            while True:
                updated_title = input("Enter the updated Title: ")
            
                # Print out error message if user does not enter a value and request to try again
                if updated_title != "":
                    cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', (updated_title, id))
                    database.commit()
                    break
                else:
                    print("Error: The entry cannot be blank. Please try again by entering a value.")
        else:
            print("Noted- no update to be made to the title.")

        # Request user if they would like to update the author of the book selected. If yes, request user to update the author and update the database.
        choice_update_author = input("Would you like to update the book author (yes/no)? ")
                
        if choice_update_author.lower() == "yes":

            while True:
                updated_author= input("Enter the updated Author: ")

                # Print out error message if user does not enter a value and request to try again
                if updated_author != "":
                    cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', (updated_author, id))
                    database.commit()
                    break
                else: 
                    print("Error: The entry cannot be blank. Please try again by entering a value.")
        else:
            print("Noted- no update to be made to the author.")

        # Request user if they would like to update the book quantity. If yes, request user to update the author and update the database.
        # Display error messages for invalid inputs for the quantity of books
        choice_update_quantity = input("Would you like to update the quantity of this book (yes/no)? ")
        
        if choice_update_quantity.lower() == "yes":

            while True:
                try: 
                    updated_quantity = int(input("Enter the updated quantity? "))
                    if updated_quantity >= 0:
                        break
                    else:
                        print("Error: Invalid input as a negative number has been entered. Please try again")
                except ValueError:
                    print("Error: Invalid input. Please try again and enter an integer number for the quantity")

            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ?''' , (updated_quantity, id))
            database.commit()

        else:
            print("Noted- no update to be made to the quantity.")

        # Print out the final updated book information of the book selected for update.
        print("The final book information is as follows: ")
        display_selected_book_in_database(id)
    

def delete_book(id):
    '''Enables user to delete selected book.

    Parameter:
        id (int): Book id

    Returns:
       Updated database where deleted book has been removed
    '''

    # Print out the database on the screen to show the books available so user can select which to delete.
    print ("The following are the books in the ebookstore database:")
    display_full_book_database()

    # Request user to enter the book id of the book details they would like to update
    # Display error messages for invalid inputs for the id entered
    while True:
        try:
            id = int(input("Please enter the id of the book you would like to delete: "))
            break
        except ValueError:
            print("Error: Invalid input for id. Please enter an integer number for the book id")

    # If book is in the database, request user to confirm if they would like to delete the book
    # If they confirm yes to deleting the book, delete the book from the database
    # If the user does not confirm to delete the book, print out message on screen to indicate that
    if display_selected_book_in_database(id) != "Book not found":

        confirmation = input("Please enter yes to confirm that you would like to delete this book from the database: ")

        if confirmation.lower() == "yes":
            cursor.execute('''DELETE FROM books WHERE id = ?''', (id,))
            database.commit()
            print("Confirmed- Book successfully deleted from database")
            display_full_book_database()

        else:
            print("Book not deleted as the deletion was not confirmed.")

def search_book():
    '''Enables user to search for a specific book'''

    # Request user to determine if they would like to search for the book based on the id, title or author
    # Display error messages for invalid inputs for the id entered
    # Print out the book information of the selected book 
    search_method = input("Would you like to search for a book using the id, title or author?: ")

    # If user selects id, request user to enter the book id of the book they would like to search
    if search_method.lower() == "id":
        while True:
            try:
                search_id = int(input("Please enter the id of the book you would like to search: "))
                if search_id > 0:
                    break
                else:
                    print("Error: Invalid input. Please enter an id  number that is greater than 0.")
            except ValueError:
                print("Error: Invalid input for id. Please enter an integer number for the book id")
        
        print("The following is the information of the book searched: ")
        display_selected_book_in_database(search_id)

    # If user selects title, request user to enter the book title of the book they would like to search
    # If the book is not found in the database, print message to notify the user of that on the screen
    # Else if the book is found in the database, print out the book information of the selected book 
    elif search_method.lower() == "title":

        search_title = input("Please enter the title of the book you would like to search: ")

        cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE LOWER (title) = ?''', (search_title.lower(),))
        book_selected = cursor.fetchone()
            
        if book_selected == None:
            print("Book not found in ebookstore database.")
            return "Book not found"

        else:
            cursor.execute('''SELECT * FROM books WHERE LOWER (title) = ?''', (search_title.lower(),))
            book_table = cursor.fetchall()
            print("The following is the information of the book searched: ")
            print (tabulate(book_table, headers = ("id", "Title", "Author", "Qty"), tablefmt="fancy_grid"))


    # If user selects title, request user to enter the book author of the book they would like to search
    # If the book is not found in the database, print message to notify the user of that on the screen
    # Else if the book is found in the database, print out the book information of the selected book 
    elif search_method.lower() == "author":

        search_author = input("Please enter the author of the book you would like to search: ")

        cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE LOWER (author) = ?''', (search_author.lower(),))
        book_selected = cursor.fetchone()
            
        if book_selected == None:
            print("Book not found in ebookstore database.")
            return "Book not found"

        else:
            cursor.execute('''SELECT * FROM books WHERE LOWER (author) = ?''', (search_author.lower(),))
            book_table = cursor.fetchall()
            print("The following is the information of the book searched: ")
            print (tabulate(book_table, headers = ("id", "Title", "Author", "Qty"), tablefmt="fancy_grid"))

    # If user does not select any of the search method options provided, print out message on screen to note that
    else:
        print("No selection made from the available search options.")


#===== Program ===========

create_database()

# Present the user with menu options and request the user to select one of them
while True:

    menu = input('''Select an option from the following menu:
                1. Enter book
                2. Update book
                3. Delete book
                4. Search books
                0. Exit''')

    if menu == "1":
        enter_book()

    elif menu == "2":
        update_book(id)

    elif menu =="3":
        delete_book(id)

    elif menu == "4":
        search_book()

    elif menu == "0":
        print('You have successfully exited. Goodbye!')

        # Close connection
        # Exit program
        database.close()
        exit()

    else:
        print("Invalid choice. Please try again by selecting a number from the menu options available.")

 
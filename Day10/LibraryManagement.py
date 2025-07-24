class Books:
    books = {}

    def __init__(self, bookId, bookName, author):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.issued_to = None  # track who borrowed the book

    def display(self):
        print(f"Book ID: {self.bookId}")
        print(f"Book Name: {self.bookName}")
        print(f"Author: {self.author}")
        status = f"Issued to User ID: {self.issued_to}" if self.issued_to else "Available"
        print(f"Status: {status}")

    @classmethod
    def addBook(cls):
        bookId = int(input("Enter Book ID: "))
        if bookId in cls.books:
            print("Book ID already exists.")
            return
        bookName = input("Enter Book Name: ")
        author = input("Enter Author: ")
        cls.books[bookId] = Books(bookId, bookName, author)
        print("Book added successfully.\n")

    @classmethod
    def showAllBooks(cls):
        if not cls.books:
            print("No books in the library.\n")
        else:
            for book in cls.books.values():
                book.display()
                print("-" * 20)


class User:
    users = {}

    def __init__(self, userId, userName):
        self.userId = userId
        self.userName = userName
        self.borrowed_books = []

    def display(self):
        print(f"User ID: {self.userId}")
        print(f"User Name: {self.userName}")
        print(f"Borrowed Books: {self.borrowed_books}")

    @classmethod
    def addUser(cls):
        userId = int(input("Enter User ID: "))
        if userId in cls.users:
            print("User ID already exists.")
            return
        userName = input("Enter User Name: ")
        cls.users[userId] = User(userId, userName)
        print("User added successfully.\n")

    @classmethod   # Class methods are bound to the class rather than an instance of the class, meaning they receive the class itself (conventionally named cls) as their first argument, instead of an instance (self). They are typically used to create factory methods or methods that operate on the class itself, rather than individual objects. 
    def showAllUsers(cls):
        if not cls.users:
            print("No users registered.\n")
        else:
            for user in cls.users.values():
                user.display()
                print("-" * 20)


class Library:

    @staticmethod  #constant in class No need of self paramenter :
    def issueBook():
        bookId = int(input("Enter Book ID to issue: "))
        userId = int(input("Enter User ID: "))

        if bookId not in Books.books:
            print("Book not found.\n")
            return
        if userId not in User.users:
            print("User not found.\n")
            return

        book = Books.books[bookId]
        user = User.users[userId]

        if book.issued_to is not None:
            print(f"Book is already issued to User ID: {book.issued_to}\n")
            return

        book.issued_to = userId
        user.borrowed_books.append(bookId)
        print("Book issued successfully.\n")

    @staticmethod
    def returnBook():
        bookId = int(input("Enter Book ID to return: "))
        userId = int(input("Enter Your User ID: "))

        if bookId not in Books.books:
            print("Book not found.\n")
            return
        if userId not in User.users:
            print("User not found.\n")
            return

        book = Books.books[bookId]
        user = User.users[userId]

        if book.issued_to != userId:
            print("This book was not issued to this user.\n")
            return

        book.issued_to = None
        user.borrowed_books.remove(bookId)
        print("Book returned successfully.\n")

    @staticmethod
    def showIssuedBooks():
        found = False
        for book in Books.books.values():
            if book.issued_to:
                book.display()
                print("-" * 20)
                found = True
        if not found:
            print("No books are currently issued.\n")


# ----------- MAIN PROGRAM LOOP -----------
def main():
    while True:
        print("\n📚 LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Add User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Show All Users")
        print("7. Show Issued Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Books.addBook()
        elif choice == '2':
            User.addUser()
        elif choice == '3':
            Library.issueBook()
        elif choice == '4':
            Library.returnBook()
        elif choice == '5':
            Books.showAllBooks()
        elif choice == '6':
            User.showAllUsers()
        elif choice == '7':
            Library.showIssuedBooks()
        elif choice == '8':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the system
if __name__ == "__main__":
    main()

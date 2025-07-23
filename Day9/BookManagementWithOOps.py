class Books:
    books = {}  # Class variable to store books

    def __init__(self, bookId=None, bookName=None, authorName=None):
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName

    def addBooks(self, bookId, bookName, authorName):
        if bookId in Books.books:
            print(f"Book ID {bookId} already exists.")
        else:
            Books.books[bookId] = {
                'bookName': bookName,
                'authorName': authorName
            }
            print("Book added successfully.")

    def searchBook(self, name):
        found = False
        for bookId, details in Books.books.items():
            if details['bookName'].lower() == name.lower():
                print(f"Book Found: ID: {bookId}, Name: {details['bookName']}, Author: {details['authorName']}")
                found = True
                break
        if not found:
            print("Book not found.")

    def removeBook(self, name):
        found = False
        for bookId in list(Books.books):
            if Books.books[bookId]['bookName'].lower() == name.lower():
                del Books.books[bookId]
                print("Book removed successfully.")
                found = True
                break
        if not found:
            print("Book not found to remove.")

    def listOfBooks(self):
        if not Books.books:
            print("No books available.")
        else:
            print("List of Books:")
            for bookId, details in Books.books.items():
                print(f"ID: {bookId}, Name: {details['bookName']}, Author: {details['authorName']}")

    def run(self):
        while True:
            print("\nEnter your choice:\n1. Add Book\n2. Search Book\n3. Remove Book\n4. List Of Books\n5. Exit")
            option = input("Choice: ")

            if option == '1':
                bookId = int(input("Enter Book ID: "))
                bookName = input("Enter Book Name: ")
                authorName = input("Enter Author Name: ")
                self.addBooks(bookId, bookName, authorName)

            elif option == '2':
                name = input("Enter Book Name to Search: ")
                self.searchBook(name)

            elif option == '3':
                name = input("Enter Book Name to Remove: ")
                self.removeBook(name)

            elif option == '4':
                self.listOfBooks()

            elif option == '5':
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")


# Run the menu
if __name__ == "__main__":
    b = Books()
    b.run()

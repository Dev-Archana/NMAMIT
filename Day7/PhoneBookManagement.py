# phonebook.py

phonebook = {}  

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print("Contact already exists.")
    else:
        number = input("Enter phone number: ").strip()
        phonebook[name] = number
        print("Contact added successfully.")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def list_contacts():
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("All Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")


while True:
    print("\n==== Phonebook Menu ====")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

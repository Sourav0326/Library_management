# main.py
from library import Library


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View User")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            copies = int(input("Enter Number of Copies: "))
            library.add_book(book_id, title, author, copies)

        elif choice == '2':
            user_id = int(input("Enter User ID: "))
            user_name = input("Enter User Name: ")
            library.register_user(user_id, user_name)

        elif choice == '3':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            library.borrow_book(user_id, book_id)

        elif choice == '4':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            library.return_book(user_id, book_id)

        elif choice == '5':
            library.view_books()

        elif choice == '6':
            user_id = int(input("Enter User ID: "))
            library.view_user(user_id)

        elif choice == '7':
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

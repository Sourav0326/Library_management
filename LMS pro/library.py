class Library:
    def __init__(self):
        self.users = {}
        self.books = []

    def add_book(self, book_id, title, author, copies):
        self.books.append((book_id, title, author, copies))
        print(f"Book {title} added successfully.")

    def register_user(self, user_id, user_name):
        if user_id not in self.users:
            self.users[user_id] = (user_name, [])
            print(f" user {user_name} registered successfully,")
        else:
            print(f"User Id {user_id} already exists")

    def borrow_book(self, user_id, book_id):
        for index, (b_id, title, author, copies) in enumerate(self.books):
            if b_id == book_id:
                if copies>0:
                    self.books[index] = (b_id, title, author, copies - 1)

                    user = self.users.get(user_id)
                    if user:
                        user_name, borrowed_books = user
                        borrowed_books.append(book_id)
                        self.users[user_id] = (user_name, borrowed_books)
                        print(f"Book '{title}' borrowed by user '{user_name}'.")
                    else:
                        print(f"User ID {user_id} not found.")
                else:
                    print(f"No copies of '{title}' are available.")
                return
                print("Book ID not found.")

    def return_book(self, user_id, book_id):
                user = self.users.get(user_id)
                if user:
                    user_name, borrowed_books = user
                    if book_id in borrowed_books:
                        borrowed_books.remove(book_id)
                        # Update user info
                        self.users[user_id] = (user_name, borrowed_books)
                        # Update book copies
                        for index, (b_id, title, author, copies) in enumerate(self.books):
                            if b_id == book_id:
                                self.books[index] = (b_id, title, author, copies + 1)
                                print(f"Book '{title}' returned by user '{user_name}'.")
                                return
                    else:
                        print("This user did not borrow this book.")
                else:
                    print("User ID not found.")

    def view_books(self):
                print("Books in the library:")
                for book_id, title, author, copies in self.books:
                    print(f"ID: {book_id}, Title: {title}, Author: {author}, Copies: {copies}")

    def view_user(self, user_id):
                user = self.users.get(user_id)
                if user:
                    user_name, borrowed_books = user
                    print(f"User: {user_name}, Borrowed Books: {borrowed_books}")
                else:
                    print("User ID not found.")
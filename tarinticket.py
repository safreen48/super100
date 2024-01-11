class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


class Member:
    def __init__(self, member_id, name, subscription_status=True):
        self.member_id = member_id
        self.name = name
        self.subscription_status = subscription_status

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Subscription: {self.subscription_status}"


class LibrarySystem:
    def __init__(self):
        self.library = Library()
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.library.find_book(book_id)

        if member and book and book.available and member.subscription_status:
            book.available = False
            print(f"{member.name} borrowed {book.title}.")
        elif not member:
            print("Member not found.")
        elif not book:
            print("Book not found.")
        elif not member.subscription_status:
            print("Member subscription is not active.")
        else:
            print("Book is not available.")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.library.find_book(book_id)

        if member and book and not book.available:
            book.available = True
            print(f"{member.name} returned {book.title}.")
        elif not member:
            print("Member not found.")
        elif not book:
            print("Book not found.")
        else:
            print("Book is already available.")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


# Example Usage
book1 = Book(1, "The Catcher in the Rye", "J.D. Salinger")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
book3 = Book(3, "1984", "George Orwell")

library_system = LibrarySystem()

library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(book3)

member1 = Member(101, "Alice")
member2 = Member(102, "Bob", False)

library_system.add_member(member1)
library_system.add_member(member2)

library_system.borrow_book(101, 1)  # Alice borrows The Catcher in the Rye
library_system.borrow_book(102, 2)  # Member subscription not active
library_system.borrow_book(103, 3)  # Member not found
library_system.borrow_book(101, 2)  # The Catcher in the Rye not available
library_system.return_book(101, 1)  # Alice returns The Catcher in the Rye
library_system.borrow_book(101, 1)  # Alice borrows The Catcher in the Rye again

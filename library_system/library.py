import json
from library_system.book import Book
from library_system.member import Member


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        return True, "Book added"

    def register_member(self, member):
        self.members[member.member_id] = member
        return True, "Member registered"

    def find_book(self, isbn):
        return self.books.get(isbn)

    def find_member(self, member_id):
        return self.members.get(member_id)

    def borrow_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if not book:
            return False, "Book not found"
        if not member:
            return False, "Member not found"
        if not member.can_borrow():
            return False, "Borrow limit reached"

        success, msg = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)

        return success, msg

    def return_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if not book or not member:
            return False, "Invalid book or member"

        success, msg = book.return_book()
        if success:
            member.return_book(isbn)

        return success, msg

    def save_data(self):
        with open("data/books.json", "w") as f:
            json.dump(
                {isbn: book.to_dict() for isbn, book in self.books.items()},
                f,
                indent=4
            )

        with open("data/members.json", "w") as f:
            json.dump(
                {mid: member.to_dict() for mid, member in self.members.items()},
                f,
                indent=4
            )

    def load_data(self):
        try:
            with open("data/books.json") as f:
                books = json.load(f)
                for isbn, data in books.items():
                    self.books[isbn] = Book.from_dict(data)
        except FileNotFoundError:
            pass

        try:
            with open("data/members.json") as f:
                members = json.load(f)
                for mid, data in members.items():
                    self.members[mid] = Member.from_dict(data)
        except FileNotFoundError:
            pass

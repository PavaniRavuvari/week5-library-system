class Member:
    """Represents a library member"""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []   # list of ISBNs
        self.max_books = 5

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, isbn):
        if not self.can_borrow():
            return False, "Borrow limit reached"
        self.borrowed_books.append(isbn)
        return True, "Book borrowed"

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True, "Book returned"
        return False, "Book not found in member records"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return f"{self.name} ({self.member_id}) - Books borrowed: {len(self.borrowed_books)}"

from library_system.library import Library
from library_system.book import Book
from library_system.member import Member


def show_menu():
    print("\n" + "=" * 40)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Save & Exit")
    print("0. Exit Without Saving")


def main():
    library = Library()
    library.load_data()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            success, msg = library.add_book(Book(title, author, isbn))
            print(msg)

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            success, msg = library.register_member(Member(name, member_id))
            print(msg)

        elif choice == "3":
            isbn = input("Book ISBN: ")
            member_id = input("Member ID: ")
            success, msg = library.borrow_book(isbn, member_id)
            print(msg)

        elif choice == "4":
            isbn = input("Book ISBN: ")
            member_id = input("Member ID: ")
            success, msg = library.return_book(isbn, member_id)
            print(msg)

        elif choice == "5":
            library.save_data()
            print("Data saved. Goodbye!")
            break

        elif choice == "0":
            print("Goodbye! Data not saved.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

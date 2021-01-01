#
# https://blog.tecladocode.com/python-30-day-14-project-regular/
#
# Day 14 Project: Reading List
#

menu_prompt = """What do you want to do?
1. Add a book
2. Search a book
3. Display your reading list
4. Quit
"""

books = "books.csv"


# Add a book: book title, author's name, year of publication
def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    with open(books, "a") as book_file:
        book_file.write(f"{title},{author},{year}\n")


def retrieve_books():
    book_shelf = []

    with open(books, "r") as book_file:
        books_data = book_file.readlines()

    for row in books_data:
        title, author, year = row.strip().split(",")

        book_shelf.append({
            "title": title,
            "author": author,
            "year": year
        })
    
    return book_shelf


# Search a book by title
def search_book():
    book_shelf = retrieve_books()
    matching_books = []

    title = input("Enter the book title: ").strip().lower()
    for book in book_shelf:
        if(title == book["title"].lower()):
            matching_books.append(book)

    return matching_books


# Display the books passed as an argument
def display_books(books):
    for book in books:
        print("- " + ", ".join(book.values()))


# Select add or display from a text menu, multiple operations allowed
def main():
    action = input(menu_prompt).strip().lower()
    while True: 
        if action == '1':
            add_book()

        elif action == '2':
            matching_books = search_book()
            if matching_books:
                display_books(matching_books)
            else:
                print("This book is not part of your reading list")

        elif action == '3':
            books = retrieve_books()
            if books:
                display_books(books)
            else:
                print("Your reading list is empty")

        elif action == '4':
            break

        else:
            print("Invalid option. Please try again.")

        action = input("Enter your next choice: ")


# Run the main program
if __name__ == "__main__":
    main()
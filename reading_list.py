#
# https://blog.tecladocode.com/python-30-day-12-project/
#
# Day 12 project: Reading list
#

reading_list = []
menu_prompt = "What do you want to do? \n 1. Add a book \n 2. Display your reading list\n 3. Quit\n"

# Add a book: book title, author's name, year of publication
def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()
    reading_list.append({
        "title": title,
        "author": author,
        "year": year
    })

# Display all the books in the reading list
def display_books():
    for book in reading_list:
        print(f"{book['title']}, {book['author']} ({book['year']})")

# Select add or display from a text menu, multiple operations allowed
while True:
    action = input(menu_prompt)
    if action == '1':
        add_book()
    elif action == '2':
        if reading_list:
            display_books()
        else:
            print("Your reading list is empty.")
    else:
        break

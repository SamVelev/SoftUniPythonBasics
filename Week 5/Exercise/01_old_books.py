search_book = input()
books_counter = 0
current_book = input()
book_is_found = False

while current_book != "No More Books":
    if current_book == search_book:
        book_is_found = True
        break
    books_counter += 1
    current_book = input()

if book_is_found:
    print(f"You checked {books_counter} books and found it."  )
else:
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")


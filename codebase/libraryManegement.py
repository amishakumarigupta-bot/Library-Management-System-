books = []


def load_books():
    try:
        f = open("library.txt", "r")
        for line in f:
            p = line.strip().split("|")      # id|title|author|status|member
            book = {"id": p[0], "title": p[1], "author": p[2],
                    "status": p[3], "member": p[4]}
            books.append(book)
        f.close()
    except FileNotFoundError:
        pass                                  # no file yet, start empty


# SAVE data to file (on exit) 
def save_books():
    f = open("library.txt", "w")
    for b in books:
        f.write(b["id"] + "|" + b["title"] + "|" + b["author"] + "|" +
                b["status"] + "|" + b["member"] + "\n")
    f.close()


#  1. ADD 
def add_book():
    title = input("Title: ")
    author = input("Author: ")
    new_id = "B" + str(101 + len(books))      # B101, B102, ...
    book = {"id": new_id, "title": title, "author": author,
            "status": "Available", "member": "-"}
    books.append(book)
    print("Book added. ID:", new_id, "|", title, "|", author, "| Available")


#2. ISSUE 
def issue_book():
    book_id = input("Book ID: ")
    for b in books:
        if b["id"] == book_id:
            if b["status"] == "Issued":
                print("Book", book_id, "is already issued.")
                return
            member = input("Member: ")
            b["status"] = "Issued"
            b["member"] = member
            print("Book", book_id, "issued to", member + ". Status: Issued")
            available = 0
            for x in books:
                if x["status"] == "Available":
                    available = available + 1
            print("Available books:", available)
            return
    print("Book ID", book_id, "not found.")


# 3. RETURN
def return_book():
    book_id = input("Book ID: ")
    for b in books:
        if b["id"] == book_id:
            b["status"] = "Available"
            b["member"] = "-"
            print("Book", book_id, "returned. Status: Available")
            return
    print("Book ID", book_id, "not found.")


#  4. SEARCH 
def search_book():
    print("1. Search by title")
    print("2. Search by author")
    choice = input("Enter choice: ")
    text = input("Enter text: ").lower()
    found = False
    for b in books:
        if choice == "1":
            match = text in b["title"].lower()
        else:
            match = text in b["author"].lower()
        if match:
            print(b["id"], "|", b["title"], "|", b["author"], "|", b["status"])
            found = True
    if found == False:
        print("No books found.")


#  5. VIEW ALL 
def view_all():
    for b in books:
        print(b["id"], "|", b["title"], "|", b["author"], "|", b["status"])


# MAIN MENU 
load_books()
while True:
    print("\n1. Add  2. Issue  3. Return  4. Search  5. View all  6. Exit")
    option = input("Enter option: ")
    if option == "1":
        add_book()
    elif option == "2":
        issue_book()
    elif option == "3":
        return_book()
    elif option == "4":
        search_book()
    elif option == "5":
        view_all()
    elif option == "6":
        save_books()
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid option.")

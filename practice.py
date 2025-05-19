import tkinter as tk
from tkinter import messagebox


books = [
    {"name": "The Hobbit", "genre": "Fantasy", "year": 1937, "available": True, "author": "J.R.R. Tolkien"},
    {"name": "1984", "genre": "Dystopian", "year": 1949, "available": False, "author": "George Orwell"},
    {"name": "To Kill a Mockingbird", "genre": "Fiction", "year": 1960, "available": True, "author": "Harper Lee"},
    {"name": "A Brief History of Time", "genre": "Science", "year": 1988, "available": True, "author": "Stephen Hawking"},
    {"name": "The Great Gatsby", "genre": "Classics", "year": 1925, "available": False, "author": "F. Scott Fitzgerald"},
    {"name": "Neuromancer", "genre": "Cyberpunk", "year": 1984, "available": True, "author": "William Gibson"},
    {"name": "Frankenstein", "genre": "Horror", "year": 1818, "available": True, "author": "Mary Shelley"},
    {"name": "Sapiens", "genre": "Non-fiction", "year": 2011, "available": True, "author": "Yuval Noah Harari"},
]

# Modify the sorting options to include author
options = [("Name", "name"), ("Genre", "genre"), ("Year", "year"), ("Author", "author")]



class LibraryBookSorter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Book Sorter")
        self.geometry("700x400")
        self.configure(bg="#333333")
        self.resizable(False, False)

        # Variables for inputs
        self.var_sort_by = tk.StringVar(value="name")
        self.var_book_name = tk.StringVar()
        self.var_only_available = tk.IntVar()

        self.create_widgets()
        self.populate_book_list(books)

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self, bg="#333333")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Right Side Panel (Book list) - moved to right side
        side_panel = tk.Frame(main_frame, bg="#222222", width=250)
        side_panel.pack(side="right", fill="y")
        side_panel.pack_propagate(False)

        label_books = tk.Label(side_panel, text="Books List", bg="#222222", fg="white", font=("Arial", 14, "bold"))
        label_books.pack(pady=(10, 5))

        # Listbox with scrollbar
        self.listbox = tk.Listbox(side_panel, bg="#111111", fg="white", font=("Arial", 11), selectbackground="#FFA500",
                                  activestyle="none")
        scrollbar = tk.Scrollbar(side_panel, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side="right", fill="y", pady=10, padx=(0, 10))

        # Left side controls frame
        controls_frame = tk.Frame(main_frame, bg="#333333")
        controls_frame.pack(side="left", fill="both", expand=True, padx=(20, 10))

        # Sort by label and options
        label_sort = tk.Label(controls_frame, text="Sort By:", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        label_sort.grid(row=0, column=0, sticky="w", pady=(10, 5))

        options = [("Name", "name"), ("Genre", "genre"), ("Year", "year"),("Author", "author")]
        for i, (text, val) in enumerate(options):
            rb = tk.Radiobutton(controls_frame, text=text, variable=self.var_sort_by, value=val, bg="#333333",
                                fg="white",
                                selectcolor="#555555", activebackground="#333333", font=("Arial", 11))
            rb.grid(row=1, column=i, padx=5, sticky="w")

        # Book name input
        label_name = tk.Label(controls_frame, text="Book Name:", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        label_name.grid(row=2, column=0, sticky="w", pady=(15, 5))
        entry_name = tk.Entry(controls_frame, textvariable=self.var_book_name, font=("Arial", 12))
        entry_name.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5)

        # Availability checkbox
        chk_available = tk.Checkbutton(controls_frame, text="Only Available", variable=self.var_only_available,
                                       bg="#333333", fg="white", selectcolor="#555555", activebackground="#333333",
                                       font=("Arial", 12))
        chk_available.grid(row=4, column=0, columnspan=3, sticky="w", pady=(15, 5))

        # Search button
        btn_search = tk.Button(controls_frame, text="Search", bg="#009900", fg="black", font=("Arial", 12, "bold"),
                               command=self.search_books, padx=10, pady=5)
        btn_search.grid(row=5, column=0, columnspan=3, sticky="ew", pady=20, padx=5)

        # Configure grid weight for inputs to expand
        controls_frame.columnconfigure(0, weight=1)
        controls_frame.columnconfigure(1, weight=1)
        controls_frame.columnconfigure(2, weight=1)

    def populate_book_list(self, book_list):
        self.listbox.delete(0, tk.END)
        if not book_list:
            self.listbox.insert(tk.END, "No books found.")
            return
        for book in book_list:
            available_text = "Available" if book["available"] else "Not Available"
            display_text = f"{book['name']} ({book['genre']}, {book['year']}) - {available_text}"
            self.listbox.insert(tk.END, display_text)

    def search_books(self):
        name_filter = self.var_book_name.get().strip().lower()
        only_available = self.var_only_available.get()
        sort_by = self.var_sort_by.get()

        # Filter books
        filtered = []
        for book in books:
            if name_filter and name_filter not in book["name"].lower():
                continue
            if only_available and not book["available"]:
                continue
            filtered.append(book)

        # Sort books
        if sort_by == "genre":
            filtered.sort(key=lambda x: x["genre"].lower())
        elif sort_by == "year":
            filtered.sort(key=lambda x: x["year"])
        elif sort_by == "author":
            filtered.sort(key=lambda x: x["author"].lower())
        else:
            filtered.sort(key=lambda x: x["name"].lower())

        # Update listbox
        self.populate_book_list(filtered)


if __name__ == "__main__":
    app = LibraryBookSorter()
    app.mainloop()


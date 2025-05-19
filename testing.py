import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Login Functionality
def login():
    username = user_entry.get().strip()
    password = password_entry.get().strip()
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="administrator",
            database="book_database"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo(title="Login", message="Login Success")
            window.withdraw()
            app = LibraryBookSorter()


# Library Book Sorter Code
class LibraryBookSorter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Book Sorter")
        self.geometry("700x400")
        self.configure(bg="#333333")
        self.resizable(False, False)

        # MySQL connection details
        self.host = "localhost"
        self.user = "root"
        self.password = "administrator"
        self.database = "book_database"

        # Variables for inputs
        self.var_sort_by = tk.StringVar(value="name")
        self.var_book_name = tk.StringVar()
        self.var_only_available = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self, bg="#333333")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Right Side Panel (Book list)
        side_panel = tk.Frame(main_frame, bg="#222222", width=250)
        side_panel.pack(side="right", fill="y")
        side_panel.pack_propagate(False)

        label_books = tk.Label(side_panel, text="Books List", bg="#222222", fg="white", font=("Arial", 14, "bold"))
        label_books.pack(pady=(10, 5))

        # Listbox with scrollbar
        self.listbox = tk.Listbox(side_panel, bg="#111111", fg="white", font=("Arial", 11), selectbackground="#FFA500")
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

        options = [("Name", "title"), ("Genre", "genre_name"), ("Year", "publication_year"), ("Author", "author_name")]
        for i, (text, val) in enumerate(options):
            rb = tk.Radiobutton(controls_frame, text=text, variable=self.var_sort_by, value=val, bg="#333333",
                                fg="white", selectcolor="#555555", activebackground="#333333", font=("Arial", 11))
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

        # Initial population of the listbox
        self.search_books()

    def populate_book_list(self, book_list):
        self.listbox.delete(0, tk.END)
        if not book_list:
            self.listbox.insert(tk.END, "No books found.")
            return
        for book in book_list:
            available_text = "Available" if book["Availability"] == "Available" else "Not Available"
            display_text = f"{book['BookTitle']} ({book['Genre']}, {book['publication_year']}) - {available_text} - {book['AuthorName']}"
            self.listbox.insert(tk.END, display_text)

    def search_books(self):
        name_filter = self.var_book_name.get().strip().lower()
        only_available = self.var_only_available.get()
        sort_by = self.var_sort_by.get()

        try:
            # Establish connection
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = connection.cursor(dictionary=True)

            # Construct the query
            query = """
            SELECT
                b.title AS BookTitle,
                a.author_name AS AuthorName,
                g.genre_name AS Genre,
                ac.category_name AS Availability,
                b.publication_year
            FROM
                books b
            JOIN
                genres g ON b.genre_id = g.genre_id
            JOIN
                availability_categories ac ON b.category_id = ac.category_id
            JOIN
                authors a ON b.author_id = a.author_id
            WHERE
                LOWER(b.title) LIKE %s
            """
            params = ('%' + name_filter + '%',)

            if only_available:
                query += " AND ac.category_name = 'Available'"

            if sort_by == "genre_name":
                query += " ORDER BY g.genre_name ASC"
            elif sort_by == "publication_year":
                query += " ORDER BY b.publication_year ASC"
            elif sort_by == "author_name":
                query += " ORDER BY a.author_name ASC"
            else:
                query += " ORDER BY b.title ASC"

            cursor.execute(query, params)
            results = cursor.fetchall()

            # Update listbox
            self.populate_book_list(results)

        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Error: {error}")
            self.populate_book_list([])
        finally:
            if connection:
                connection.close()

if __name__ == "__main__":
    window.mainloop()

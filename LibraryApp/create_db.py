import sqlite3

# Create a connection to the database
conn = sqlite3.connect('books_authors.db')
cursor = conn.cursor()

# Create the author table
cursor.execute('''CREATE TABLE IF NOT EXISTS author (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    birth_date DATE NOT NULL,
                    birth_place TEXT NOT NULL)''')

# Create the book table
cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    page_count INTEGER NOT NULL,
                    publish_date DATE NOT NULL,
                    author_id INTEGER NOT NULL,
                    FOREIGN KEY (author_id) REFERENCES author(id))''')

# Commit the table creation
conn.commit()

# Close the connection
conn.close()

print("Database and tables created successfully!")

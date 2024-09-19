import sqlite3
from datetime import date, datetime

# Connect to the existing database
conn = sqlite3.connect('books_authors.db')
cursor = conn.cursor()

# Query to find the book with the most pages and join with the author table
cursor.execute('''
    SELECT book.id, book.title, book.page_count, book.category, book.publish_date, 
           author.first_name, author.last_name, author.birth_place
    FROM book
    JOIN author ON book.author_id = author.id
    WHERE book.page_count = (SELECT MAX(page_count) FROM book)
''')

# Fetch the results
most_pages_book = cursor.fetchall()

# Print the book details along with the author's information
print("Book with the most pages and its author:")
for book in most_pages_book:
    print(f"Book ID: {book[0]}, Title: {book[1]}, Pages: {book[2]}, Category: {book[3]}, "
          f"Publish Date: {book[4]}, Author: {book[5]} {book[6]}, Birthplace: {book[7]}")

cursor.execute('''SELECT AVG(page_count) FROM book''')
average_page_books = cursor.fetchone()[0]
print("average page book:", int(average_page_books))

cursor.execute('''SELECT * FROM author ORDER BY birth_date DESC LIMIT 1''')
youngest_author = cursor.fetchone()
name = youngest_author[1]
surname = youngest_author[2]
today = date.today()

# Convert the birth_date string to a datetime.date object
youngest_author_birth_date = datetime.strptime(youngest_author[3], '%Y-%m-%d').date()

# Calculate the author's age in days
author_age_days = (today - youngest_author_birth_date).days

# Convert the age from days to years
author_age_years = author_age_days // 365
print("author_age:", author_age_years)

cursor.execute('''SELECT * FROM author WHERE id NOT IN (SELECT author_id FROM book)''')
authors_without_books = cursor.fetchall()
print(f"{len(authors_without_books)} Authors without books:")

for author in authors_without_books:
    print(author[1], author[2])

# Query to find authors with more than 3 books
cursor.execute('''
    SELECT author.id, author.first_name, author.last_name, COUNT(book.id) as book_count
    FROM author
    JOIN book ON author.id = book.author_id
    GROUP BY author.id
    HAVING book_count > 3
    LIMIT 5
''')

# Fetch the results
authors_with_many_books = cursor.fetchall()

# Print the results
print("Authors with more than 3 books:")
for author in authors_with_many_books:
    print(f"ID: {author[0]}, Name: {author[1]} {author[2]}, Number of Books: {author[3]}")

# Close the connection
conn.close()

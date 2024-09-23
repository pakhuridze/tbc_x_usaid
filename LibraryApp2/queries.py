from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from create_db import Author, Book, engine
from datetime import date

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# 1. Query to find the book with the most pages and join with the author table
most_pages_book = session.query(Book, Author).join(Book.authors).order_by(Book.page_count.desc()).first()

if most_pages_book:
    book, author = most_pages_book
    print("Book with the most pages and its author:")
    print(f"Book ID: {book.id}, Title: {book.title}, Pages: {book.page_count}, Category: {book.category}, "
          f"Publish Date: {book.publish_date}, Author: {author.first_name} {author.last_name}, Birthplace: {author.birth_place}")

# 2. Calculate the average number of pages in all books
average_page_books = session.query(func.avg(Book.page_count)).scalar()
print("Average page count of all books:", int(average_page_books))

# 3. Find the youngest author based on birth_date
youngest_author = session.query(Author).order_by(Author.birth_date.desc()).first()

if youngest_author:
    today = date.today()
    youngest_author_birth_date = youngest_author.birth_date
    author_age_days = (today - youngest_author_birth_date).days
    author_age_years = author_age_days // 365
    print(f"Youngest author: {youngest_author.first_name} {youngest_author.last_name}, Age: {author_age_years}")

# 4. Find authors without books
authors_without_books = session.query(Author).filter(~Author.books.any()).all()
print(f"{len(authors_without_books)} Authors without books:")

for author in authors_without_books:
    print(author.first_name, author.last_name)

# 5. Query to find authors with more than 3 books
authors_with_many_books = (session.query(Author, func.count(Book.id).label('book_count'))
                           .join(Author.books)
                           .group_by(Author.id)
                           .having(func.count(Book.id) > 3)
                           .limit(5)
                           .all())

# Print the results
print("Authors with more than 3 books:")
for author, book_count in authors_with_many_books:
    print(f"ID: {author.id}, Name: {author.first_name} {author.last_name}, Number of Books: {book_count}")

# Close the session
session.close()

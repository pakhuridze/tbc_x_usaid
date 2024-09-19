# LibraryApp

This project is a Python application that generates a library of books and authors, stores them in an SQLite database, and allows you to run various SQL queries to analyze the data.

## Features

### Random Data Generation
- 500 randomly generated authors (with names, birth dates, and cities).
- 1000 randomly generated books associated with the authors (with titles, categories, page counts, and publish dates).

### Database Queries
- Fetch the book with the most pages and its author’s details.
- Calculate the average number of pages across all books.
- Find the youngest author and calculate their age.
- List authors without any books.
- List authors who have written more than 3 books.

## Technologies
- **Python**: Core programming language.
- **SQLite**: Lightweight relational database.
- **Faker**: Library used to generate random data.
- **Random**: Standard library for random operations.

## Usage

```bash
##create db :
python create_db.py

##generate data

python generate_data.py

## do queries

python queries.py
```
## LibraryApp - Queries
Script: queries.py
1. Book with the Most Pages
2. Average Number of Pages in Books
3. Youngest Author
4. Authors Without Books
5. Authors with More Than 3 Books
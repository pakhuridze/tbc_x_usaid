# Books and Authors Database

This project is a demonstration of using SQLAlchemy with Faker to populate a SQLite database with random authors and books. It includes scripts to generate data and perform various queries on the database.

## Project Structure

- `create_db.py`: Contains the SQLAlchemy models for `Author` and `Book`, and the database setup.
- `generate_data.py`: Populates the database with random authors and books using Faker.
- `queries.py`: Contains various queries to interact with the database.

## Getting Started

### Prerequisites

- Python 3.x
- SQLAlchemy
- Faker

### Installation

1. Clone the repository:
    ```sh
    https://github.com/pakhuridze/tbc_x_usaid/
    cd LibraryApp2
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Create the database and tables:
    ```sh
    python create_db.py
    ```

2. Populate the database with random data:
    ```sh
    python populate_db.py
    ```

3. Run the queries:
    ```sh
    python queries.py
    ```

## Queries

The `queries.py` script includes the following queries:

1. **Find the book with the most pages and its author**:
    ```python
    most_pages_book = session.query(Book, Author).join(Book.authors).order_by(Book.page_count.desc()).first()
    ```

2. **Calculate the average number of pages in all books**:
    ```python
    average_page_books = session.query(func.avg(Book.page_count)).scalar()
    ```

3. **Find the youngest author based on birth date**:
    ```python
    youngest_author = session.query(Author).order_by(Author.birth_date.desc()).first()
    ```

4. **Find authors without books**:
    ```python
    authors_without_books = session.query(Author).filter(~Author.books.any()).all()
    ```

5. **Find authors with more than 3 books**:
    ```python
    authors_with_many_books = (session.query(Author, func.count(Book.id).label('book_count'))
                               .join(Author.books)
                               .group_by(Author.id)
                               .having(func.count(Book.id) > 3)
                               .all())
    ```

## Acknowledgments

- Faker
- SQLAlchemy


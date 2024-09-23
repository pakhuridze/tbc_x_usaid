import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import Author, Book

# Initialize Faker and database connection
fake = Faker()
engine = create_engine('sqlite:///books_authors.db')
Session = sessionmaker(bind=engine)
session = Session()

# Generate 500 random authors
authors = [
    Author(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date_of_birth(minimum_age=10, maximum_age=100),
        birth_place=fake.city()
    )
    for _ in range(500)
]

# Add authors to the session
session.add_all(authors)
session.commit()

# Fetch all authors with their IDs
all_authors = session.query(Author).all()

# Predefined list of book categories
categories = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance']


# Function to generate a valid book publish date
def generate_valid_publish_date(birth_date):
    # The earliest publish date should be 10 years after the author's birth date
    min_publish_date = birth_date + timedelta(days=365 * 10)
    max_publish_date = datetime.now().date()
    # Return a random date between these two limits
    return fake.date_between(min_publish_date, max_publish_date)


# Generate and insert 1000 books with authors
for _ in range(1000):
    # Randomly select 1-3 authors for each book
    selected_authors = random.sample(all_authors, random.randint(1, 3))

    # Generate book details
    publish_date = generate_valid_publish_date(selected_authors[0].birth_date)
    book = Book(
        title=fake.sentence(nb_words=4),
        category=random.choice(categories),
        page_count=random.randint(50, 1000),
        publish_date=publish_date
    )

    # Add authors to the book
    book.authors.extend(selected_authors)

    # Add book to the session
    session.add(book)

# Commit all the changes
session.commit()  # Close the session

# Close Session
session.close()
print("Authors and books inserted successfully!")

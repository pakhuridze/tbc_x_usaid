import random
import sqlite3
from datetime import datetime, timedelta

from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to the existing database
conn = sqlite3.connect('books_authors.db')
cursor = conn.cursor()

# Generate 500 random authors
authors = [
    (
        fake.first_name(),  # first_name
        fake.last_name(),  # last_name
        fake.date_of_birth(minimum_age=10, maximum_age=100).isoformat(),  # birth_date as ISO format string
        fake.city()  # birth_place
    )
    for _ in range(500)
]

# Insert authors into the database
cursor.executemany('''INSERT INTO author (first_name, last_name, birth_date, birth_place) 
                      VALUES (?, ?, ?, ?)''', authors)

# Commit the author insertions
conn.commit()

# Fetch all author IDs and birthdates
cursor.execute('SELECT id, birth_date FROM author')
authors_data = cursor.fetchall()

# Predefined list of book categories
categories = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance']


# Function to generate a valid book publish date
def generate_valid_publish_date(birth_date):
    # Convert birth_date from string to date object
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
    # The earliest publish date should be 10 years after the author's birth date
    min_publish_date = birth_date + timedelta(days=365 * 10)  # Adding 10 years
    # The latest publish date is today
    max_publish_date = datetime.now().date()
    # Return a random date between these two limits
    return fake.date_between(min_publish_date, max_publish_date).isoformat()


# Generate and insert 1000 books
books = []
for _ in range(1000):
    # Randomly select an author
    author_id, birth_date = random.choice(authors_data)

    # Generate a valid publish date
    publish_date = generate_valid_publish_date(birth_date)

    # Generate book details
    book = (
        fake.sentence(nb_words=4),  # title
        random.choice(categories),  # category
        random.randint(50, 1000),  # page_count
        publish_date,  # publish_date as ISO format string
        author_id  # author_id
    )

    books.append(book)

# Insert books into the database
cursor.executemany('''INSERT INTO book (title, category, page_count, publish_date, author_id) 
                      VALUES (?, ?, ?, ?, ?)''', books)

# Commit the book insertions
conn.commit()

# Close the connection
conn.close()

print("Authors and books inserted successfully!")

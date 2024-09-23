from sqlalchemy import create_engine, Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Initialize the base class for ORM models
Base = declarative_base()

# Define a many-to-many relationship table between authors and books
author_book_association = Table(
    'author_book', Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id')),
    Column('book_id', Integer, ForeignKey('book.id'))
)


# Define the Author model
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    birth_place = Column(String, nullable=False)

    # Relationship to books through the association table
    books = relationship('Book', secondary=author_book_association, back_populates='authors')


# Define the Book model
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    page_count = Column(Integer, nullable=False)
    publish_date = Column(Date, nullable=False)

    # Relationship to authors through the association table
    authors = relationship('Author', secondary=author_book_association, back_populates='books')


# Database setup
engine = create_engine('sqlite:///books_authors.db')
Base.metadata.create_all(engine)
if __name__ == '__main__':
    print("Database and tables created successfully!")

# David Wylie
# CIS256 Term (Fall 2025)
# Extra Credit Assignment
# sqlite_example.py - refactored to add decorator for logging function timing

import sqlite3
import csv
from pathlib import Path
from timelogger import timelog


@timelog('file_timelog.txt')
def get_publishers():
    """
    Gets the pubisher information from the publishers.csv
    return: tuple of publisher information.
    """
    p = Path(__file__).with_name('publishers.csv')
    with p.open('r', newline='') as f:
        reader = csv.reader(f)
        publisher_data = [(int(row[0]), row[1]) for row in reader]

    return publisher_data


@timelog('file_timelog.txt')
def get_authors():
    """
    Gets the author information from the authors.csv
    return: tuple of author information.
    """
    p = Path(__file__).with_name('authors.csv')
    with p.open('r', newline='') as f:
        reader = csv.reader(f)
        author_data = [(int(row[0]), row[1], row[2]) for row in reader]

    return author_data


@timelog('file_timelog.txt')
def get_books_authors():
    """
    Gets the author information from the books_authors.csv
    return: tuple of books_author information.
    """
    p = Path(__file__).with_name('books_authors.csv')
    with p.open('r', newline='') as f:
        reader = csv.reader(f)
        books_authors_data = [(int(row[0]), int(row[1]), int(row[2])) for row in reader]

    return books_authors_data


def int_or_blank(value):
    try:
        return int(value)
    except ValueError:
        return ''


@timelog('file_timelog.txt')
def get_books():
    """
    Gets the book information from the books.csv
    return: tuple of books information.
    """
    p = Path(__file__).with_name('books.csv')
    with p.open('r', newline='') as f:
        reader = csv.reader(f)
        book_data = [(int(row[0]), row[1], int_or_blank(row[2]), int(row[3])) for row in reader]

    return book_data


@timelog('file_timelog.txt')
def create_publishers_table():
    """
    Creates/Updates publishers table.
    param: tuple of publisher information.
    """
    p = Path(__file__).with_name('booksdb.sqlite')
    dbconn = sqlite3.connect(p.resolve())
    dbconn.execute("PRAGMA foreign_keys = 1")

    dbconn.execute("""CREATE TABLE IF NOT EXISTS publishers
                    (publisher_id INT PRIMARY KEY NOT NULL,
                    publisher_name TEXT NOT NULL,
                    UNIQUE(publisher_name));
                    """)

    dbconn.executemany("INSERT  or IGNORE into publishers (publisher_id,publisher_name) VALUES (?,?)", get_publishers())
    dbconn.commit()

    cursor = dbconn.execute("""SELECT publisher_id,publisher_name FROM publishers;""")

    for row in cursor:
        print(f"""
        publisher_id: {row[0]}
        publisher_name: {row[1]}""")

    dbconn.close()


@timelog('file_timelog.txt')
def create_authors_table():
    """
    Creates/Updates authors table.
    param: tuple of authors information.
    """
    p = Path(__file__).with_name('booksdb.sqlite')
    dbconn = sqlite3.connect(p.resolve())
    dbconn.execute("PRAGMA foreign_keys = 1")

    dbconn.execute("""CREATE TABLE IF NOT EXISTS authors
                    (author_id INT PRIMARY KEY NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NULL,
                    UNIQUE(last_name,first_name));
                    """)

    dbconn.executemany("INSERT  or IGNORE into authors (author_id,first_name,last_name) VALUES (?,?,?)", get_authors())
    dbconn.commit()

    cursor = dbconn.execute("""SELECT author_id,first_name,last_name FROM authors;""")

    for row in cursor:
        print(f"""
        author_id: {row[0]}
        first_name: {row[1]}
        last_name: {row[2]}""")

    dbconn.close()


@timelog('file_timelog.txt')
def create_books_table():
    """
    Creates/Updates books table.
    param: tuple of books information.
    """
    p = Path(__file__).with_name('booksdb.sqlite')
    dbconn = sqlite3.connect(p.resolve())
    dbconn.execute("PRAGMA foreign_keys = 1")

    dbconn.execute("""CREATE TABLE IF NOT EXISTS books
                (book_id INT PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                yearpub INT NOT NULL,
                publisher_id INT NOT NULL,
                UNIQUE(title),
                FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id));
                """)

    dbconn.executemany("INSERT  or IGNORE into books (book_id,title,yearpub,publisher_id) VALUES (?,?,?,?)", get_books())
    dbconn.commit()

    cursor = dbconn.execute("""select book_id, title, yearpub, publisher_id  from books;""")

    for row in cursor:
        print(f"""
        book_id: {row[0]}
        title: {row[1]}
        yearpub: {row[2]}
        publisher_id: {row[3]}
        """)

    dbconn.close()


@timelog('file_timelog.txt')
def create_books_authors_table():
    """
    Creates/Updates books_authors table.
    param: tuple of books_authors information.
    """
    p = Path(__file__).with_name('booksdb.sqlite')
    dbconn = sqlite3.connect(p.resolve())
    dbconn.execute("PRAGMA foreign_keys = 1")

    dbconn.execute("""CREATE TABLE IF NOT EXISTS books_authors
                    (book_id INT,
                    author_id INT,
                    author_order INT,
                    FOREIGN KEY(book_id) REFERENCES books(book_id),
                    FOREIGN KEY(author_id) REFERENCES authors(author_id));
                    """)

    dbconn.executemany("INSERT  or IGNORE into books_authors (book_id, author_id, author_order) VALUES (?,?,?)", get_books_authors())
    dbconn.commit()

    cursor = dbconn.execute("SELECT book_id, author_id, author_order from books_authors;")

    for row in cursor:
        print(f"""
        book_id: {row[0]}
        author_id: {row[1]}
        author_order: {row[2]}
        """)

    dbconn.close()


@timelog('file_timelog.txt')
def query_all_tables():
    """
    Queries all Tables with inner joins, prints out information about books
    """
    p = Path(__file__).with_name('booksdb.sqlite')
    dbconn = sqlite3.connect(p.resolve())
    dbconn.execute("PRAGMA foreign_keys = 1")

    cursor = dbconn.execute("""SELECT b.title, b.yearpub,a.first_name,a.last_name,ba.author_order,p.publisher_name
                            FROM books AS b INNER JOIN books_authors AS ba ON b.book_id = ba.book_id
                            INNER JOIN authors AS a ON a.author_id = ba.author_id
                            INNER JOIN publishers AS p  ON p.publisher_id = b.publisher_id;
                            """)

    for row in cursor:
        print(f"""
        title: {row[0]}
        year published: {row[1]} 
        Author: {row[2]} {row[3]}
        Author Order: {row[4]}
        Publisher: {row[5]}
        """)

    cursor = dbconn.execute("""SELECT name FROM sqlite_master 
                                WHERE type ='table' 
                                AND 
                                name NOT LIKE 'sqlite_%';""")
    print("List of Tables in Database")

    for row in cursor:
        print(f"""table: {row[0]} """)

    dbconn.close()


if __name__ == "__main__":
    create_publishers_table()
    create_authors_table()
    create_books_table()
    create_books_authors_table()
    query_all_tables()

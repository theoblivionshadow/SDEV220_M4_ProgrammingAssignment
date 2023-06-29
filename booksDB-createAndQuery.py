'''
Shadow R.
SDEV 220
M04 Programming Assignment
06.29.2023
Purpose:
    create a database to store book titles, authors, and publication years
    populate table from csv file
    query using sqlite3 and sqlalchemy
        get titles by pub year
        get titles by alphabetical order
'''

#import libs
import sqlite3
import csv
import os
from sqlalchemy import create_engine, text

#create connection & cursor
conn = sqlite3.connect('books.db')
curs = conn.cursor()

#check if db exists
#delete the table and it's contents so the code can run without errors
### would not use this in an actual database, but using this here to
### make the assignment run smoothly for testing & grading purposes
if os.path.exists('books.db') == True:
    curs.execute('DROP TABLE books')
else:
    pass

# create table books with columns/attributes
# of title, author and year with title as PK        
curs.execute('''CREATE TABLE books
    (title VARCHAR(50) PRIMARY KEY,
    author VARCHAR(40),
    year INT)
    ''')

# open csv of book data & read it
with open('books2.csv','rt') as fin:
    cin = csv.DictReader(fin)
    # save book data to a list
    books2 = [row for row in cin]

# var to store SQL command to populate table
ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'

# loop to populate table
for data in books2:
    # take each book data collection from books as 'data' to get dictionarys
    # use .get() to grab individual attribute values
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')
    # use .execute() to call ins variable with SQL command & populate 
    # table with saved attribute values
    curs.execute(ins, (title, author, year))
    # .commit() to save changes to DB.
    '''
    !!! without this, run risk of:

    OperationalError: database is locked

    this means that too many cursors are attempting to make changes 
    at the same time to the DB
    '''
    conn.commit()

'''
# code below used to check success of populating data into the table
# for each record, print all attibute values

for row in curs.execute('SELECT * FROM books'):
    print(row)
'''

# for each record, print titles only with newest book first
for row in curs.execute('SELECT title FROM books ORDER BY year DESC'):
    print(row)


# sqlalchemy below

# create connection
eng = create_engine('sqlite:///books.db')
conn = eng.connect()

# create query command to get book titles in alphabetical order
# default order is ascending - no need to specify
query = text("SELECT title FROM books ORDER BY title")

# execute query command and save results in variable
result = conn.execute(query).fetchall()

#formatting, separates previous query w/ sqlite3 from sqlalchemy
print()

# print titles in alphabetical order
for record in result:
    print(record)
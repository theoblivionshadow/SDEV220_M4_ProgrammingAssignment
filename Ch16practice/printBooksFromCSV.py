'''
Shadow R.
SDEV 220
M04 - Ch 16.1 & 16.2 Things to do

books.cvs for 16.1 created outside py file here
'''

import csv

with open('books.csv','rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)
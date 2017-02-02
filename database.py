import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''
CREATE TABLE tbl1(id INTEGER PRIMARY KEY ASC, name VARCHAR(50), number VARCHAR(250))
''')

tbl1_insert_values = [
(1,'josh voss','8609314521'),
(2,'teresa cramer','6165236657'),
(3,'robert half','6160025453'),
(4,'kforce','6169967789'),
(5,'teksystems','6161145100')
]

c.executemany('''
INSERT INTO tbl1(id, name, number)
VALUES (?, ?, ?)
''', tbl1_insert_values)
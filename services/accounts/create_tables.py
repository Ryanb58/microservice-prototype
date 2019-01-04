import sqlite3

import os

sqlite_file = 'app.sqlite'    # name of the sqlite database file

if os.path.exists(sqlite_file):
  os.remove(sqlite_file)
else:
  print("The file does not exist")

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
# c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#         .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
# c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
#         .format(tn=table_name1, nf=new_field, ft=field_type))
try:
    c.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, fullname TEXT, email TEXT unique, password TEXT, confirm_token TEXT, password_reset_token TEXT)')
except sqlite3.OperationalError:
    pass

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
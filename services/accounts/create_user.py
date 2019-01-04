import sqlite3

sqlite_file = 'app.sqlite'    # name of the sqlite database file

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

c.execute('''INSERT INTO users(name, fullname, email, password)
                  VALUES(?,?,?,?)''', ('Admin', 'Administrator', 'admin@example.com', 'password'))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
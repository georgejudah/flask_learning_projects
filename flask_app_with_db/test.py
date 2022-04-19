# import sqlite3


# connection = sqlite3.connect('data.db')

# cursor = connection.cursor()

# create_table = "CREATE TABLE users (id int, username text, password text)"

# cursor.execute(create_table)

# user = (1, 'judah', 'password')

# insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# cursor.execute(insert_query, user)

# users = [
#     (2, 'justin', 'passa123'),
#     (3, 'julia', 'xtension')
# ]

# cursor.executemany(insert_query, users)

# select_query = "SELECT * FROM users WHERE username LIKE 'j%' "
# for row in cursor.execute(select_query):
#     print(row)

# connection.commit()

# connection.close()
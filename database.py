import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    release_date DATE)''')

movies = [('Movie 1', 'Something about the movie', '2023-06-08'),
          ('Movie 2', 'Something about the movie', '2023-06-08'),
          ('Movie 3', 'Something about the movie', '2023-06-08'),
          ('Movie 4', 'Something about the movie', '2023-06-08'),
          ('Movie 5', 'Something about the movie', '2023-06-08')]

cursor.executemany("INSERT INTO Movies (title, description, release_date) VALUES (?,?,?)", movies)


conn.commit()

conn.close()
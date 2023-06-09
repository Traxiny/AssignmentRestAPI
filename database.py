import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    release_year DATE)''')

movies = [('Movie 1', 'Something about the movie', '2023'),
          ('Movie 2', 'Something about the movie', '2019'),
          ('Movie 3', 'Something about the movie', '2020'),
          ('Movie 4', 'Something about the movie', '2021'),
          ('Movie 5', 'Something about the movie', '2022')]

cursor.executemany("INSERT INTO Movies (title, description, release_year) VALUES (?,?,?)", movies)


conn.commit()

conn.close()
from flask import Flask, jsonify, request, Response
import sqlite3
import json

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_all_movies():
    with sqlite3.connect("test.db") as conn:
        app.config['DATABASE'] = conn
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Movies")
        rows = cursor.fetchall()

    if rows is None:
        return jsonify({'error': 'Movie not found'}), 404
    
    movies = []
    for row in rows:
        movie = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'release_year': row[3]
        }
        movies.append(movie)

    json_string = json.dumps(movies)
    response = json_string.replace(',', '\n')
    return Response(response, content_type='application/json')

@app.route('/movies/<int:id>',methods=['GET'])
def get_movie_by_id(id):
    with sqlite3.connect("test.db") as conn:
        app.config['DATABASE'] = conn
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Movies WHERE id == ?",(id,))
        row = cursor.fetchone()

    if row is None:
        return jsonify({'error': 'Movie not found'}), 404
    
    movie = {
        'id': row[0],
        'title': row[1],
        'description': row[2],
        'release_year': row[3]
    }

    return jsonify(movie)

@app.route('/movies',methods=['POST'])
def create_movie():
    new_movie = request.get_json()
    if new_movie and 'title' in new_movie and 'release_year' in new_movie:
        with sqlite3.connect("test.db") as conn:
            app.config['DATABASE'] = conn
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Movies (title, description, release_year) VALUES (:title, :description, :release_year)", new_movie)
        return jsonify({'response': 'All went good'})
    else:
        return jsonify({'error': 'Bad Request status'}), 400


@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    new_movie = request.get_json()
    set_clause = ', '.join([f'{key} = ?' for key in new_movie.keys()])
    if new_movie:
        with sqlite3.connect("test.db") as conn:
            app.config['DATABASE'] = conn
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Movies WHERE id == ?",(id,))
            row = cursor.fetchone()
            if row is None:
                return jsonify({'error': 'Movie not found'}), 404
            values = list(new_movie.values()) + [id]
            cursor.execute(f"UPDATE Movies SET {set_clause} WHERE id == ?", values)
            cursor.execute("SELECT * FROM Movies WHERE id == ?",(id,))
            row = cursor.fetchone()

        movie = {
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'release_year': row[3]
        }

        return jsonify(movie)
    else:
        return jsonify({'error': 'Bad Request status'}), 400

if __name__ == '__main__':
    app.run()   

@app.teardown_appcontext
def close_connection(exception):
    conn = app.config.get('DATABASE')
    if conn is not None:
        conn.close()
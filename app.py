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
            'release_date': row[3]
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
        'release_date': row[3]
    }

    return jsonify(movie)

if __name__ == '__main__':
    app.run()   

@app.teardown_appcontext
def close_connection(exception):
    conn = app.config.get('DATABASE')
    if conn is not None:
        conn.close()
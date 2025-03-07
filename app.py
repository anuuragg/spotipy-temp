from flask import Flask, render_template, request
from function import search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    artist = request.form.get('artist')
    songs = search(artist)
    return render_template('songs.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)


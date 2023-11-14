from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os
import random
import watchdog
app = Flask(__name__)
CORS(app)

playlist = [
    { "title": "Song1","file": "song1.mp3"},
    {"title": "Song 2", "file": "song2.mp3"},
 {"title": "Song 3", "file": "song3.mp3"},
 {"title": "Song 4", "file": "song4.mp3"},
 {"title": "Song 5", "file": "song5.mp3"},
 {"title": "Song 6", "file": "song6.mp3"},
 {"title": "Song 7", "file": "song7.mp3"},
 {"title": "Song 8", "file": "song8.mp3"},
 {"title": "Song 9", "file": "song9.mp3"},
 {"title": "Song 10", "file": "song10.mp3"},
 {"title": "Song 11", "file": "song11.mp3"},
 {"title": "Song 12", "file": "song12.mp3"},
 {"title": "Song 13", "file": "song13.mp3"},
 {"title": "Song 14", "file": "song14.mp3"},
 {"title": "Song 15", "file": "song15.mp3"},
 {"title": "Song 16", "file": "song16.mp3"},
 {"title": "Song 17", "file": "song17.mp3"},
 {"title": "Song 18", "file": "song18.mp3"},
 {"title": "Song 19", "file": "song19.mp3"},
 {"title": "Song 21", "file": "song20.mp3"},
 {"title": "Song 22", "file": "song22.mp3"},
 {"title": "Song 23", "file": "song23.mp3"},
 {"title": "Song 24", "file": "song24.mp3"},
 {"title": "Song 25", "file": "song25.mp3"},
 {"title": "Song 26", "file": "song26.mp3"},
 {"title": "Song 27", "file": "song27.mp3"},
 {"title": "Song 28", "file": "song28.mp3"},
 {"title": "Song 29", "file": "song29.mp3"},
 {"title": "Song 30", "file": "song30.mp3"},
 {"title": "Song 31", "file": "song31.mp3"},
 {"title": "Song 32", "file": "song32.mp3"},
 {"title": "Song 33", "file": "song33.mp3"},
 {"title": "Song 34", "file": "song34.mp3"},
 {"title": "Song 35", "file": "song35.mp3"},
 {"title": "Song 36", "file": "song36.mp3"},
 {"title": "Song 37", "file": "song37.mp3"},
 {"title": "Song 38", "file": "song38.mp3"},
 {"title": "Song 39", "file": "song39.mp3"},
 {"title": "Song 40", "file": "song40.mp3"},
 {"title": "Song 41", "file": "song41.mp3"},
 {"title": "Song 42", "file": "song42.mp3"},
 {"title": "Song 43", "file": "song43.mp3"},
 {"title": "Song 44", "file": "song44.mp3"},
 {"title": "Song 45", "file": "song45.mp3"},
 {"title": "Song 46", "file": "song46.mp3"},
 {"title": "Song 47", "file": "song47.mp3"},
 {"title": "Song 48", "file": "song48.mp3"},
 {"title": "Song 49", "file": "song49.mp3"},
 {"title": "Song 50", "file": "song50.mp3"}
]

current_song_index = 0
shuffle_mode = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_playlist')
def get_playlist():
    return jsonify(playlist)


@app.route('/play')
def play():
    global current_song_index
    song = playlist[current_song_index]
    return jsonify({'status': 'success', 'message': 'Song is playing', 'file': song['file']})


@app.route('/pause')
def pause():
    return jsonify({'status': 'success', 'message': 'Song is paused'})


@app.route('/next')
def next_song():
    global current_song_index
    current_song_index = get_next_song_index()
    return play()


@app.route('/previous')
def previous_song():
    global current_song_index
    current_song_index = get_previous_song_index()
    return play()


@app.route('/toggle_shuffle')
def toggle_shuffle():
    global shuffle_mode
    shuffle_mode = not shuffle_mode
    return jsonify({'status': 'success', 'shuffle_mode': shuffle_mode})


def get_next_song_index():
    if shuffle_mode:
        return random.randint(0, len(playlist) - 1)
    else:
        return (current_song_index + 1) % len(playlist)


def get_previous_song_index():
    if shuffle_mode:
        return random.randint(0, len(playlist) - 1)
    else:
        return (current_song_index - 1) % len(playlist)


if __name__ == '__main__':
    app.run(debug=True)

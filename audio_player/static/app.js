document.addEventListener('DOMContentLoaded', function () {
    fetch('/get_playlist')
        .then(response => response.json())
        .then(data => {
            const playlistElement = document.getElementById('playlist');
            data.forEach(song => {
                const listItem = document.createElement('div');
                listItem.innerText = song.title;
                playlistElement.appendChild(listItem);
            });
        });

    fetch('/toggle_shuffle')
        .then(response => response.json())
        .then(data => {
            const shuffleModeElement = document.getElementById('shuffleMode');
            shuffleModeElement.innerText = `Shuffle Mode: ${data.shuffle_mode ? 'On' : 'Off'}`;
        });

    // Set up the audio player and listen for the 'ended' event
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.addEventListener('ended', function () {
        // Call the 'next' function when the current song ends
        next();
    });

    // Display the name of the currently playing song
    const currentSongElement = document.getElementById('currentSong');
    currentSongElement.innerText = "Now Playing: None";
});

function togglePlayPause() {
    const audioPlayer = document.getElementById('audioPlayer');
    const isPlaying = !audioPlayer.paused;

    if (isPlaying) {
        audioPlayer.pause();
    } else {
        fetch('/play')
            .then(response => response.json())
            .then(data => {
                updateCurrentSong(data.file);
                audioPlayer.src = `static/audio/${data.file}`;
                audioPlayer.play();
            });
    }
}

function updateCurrentSong(songName) {
    const currentSongElement = document.getElementById('currentSong');
    currentSongElement.innerText = `Now Playing: ${songName}`;
}

function next() {
    fetch('/next')
        .then(response => response.json())
        .then(data => {
            updateCurrentSong(data.file);
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = `static/audio/${data.file}`;
            audioPlayer.play();
        });
}

function previous() {
    fetch('/previous')
        .then(response => response.json())
        .then(data => {
            updateCurrentSong(data.file);
            const audioPlayer = document.getElementById('audioPlayer');
            audioPlayer.src = `static/audio/${data.file}`;
            audioPlayer.play();
        });
}

function toggleShuffle() {
    fetch('/toggle_shuffle')
        .then(response => response.json())
        .then(data => {
            const shuffleModeElement = document.getElementById('shuffleMode');
            shuffleModeElement.innerText = `Shuffle Mode: ${data.shuffle_mode ? 'On' : 'Off'}`;
        });
}

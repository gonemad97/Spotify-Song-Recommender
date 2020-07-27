from flask import *
import Search

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("search.html")

@app.route('/success',methods=['POST'])
def top_k():
    global query
    if request.method == 'POST':
        song_name = request.form['song']
        artist_name = request.form['artist']
        # artist:Selena Gomez track:Look At Her Now
        similar_songs = Search.display_songs("artist:" + artist_name + " " + "track:" + song_name)

    return render_template('output.html',tables=[similar_songs.to_html()],
                           titles = ['na', "Similar songs"])


if __name__ == '__main__':
    app.run(debug = True)
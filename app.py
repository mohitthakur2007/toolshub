from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        file_path = video_stream.download()
        return file_path
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        file_path = download_video(video_url)

        if file_path:
            return render_template('success.html', file_path=file_path)
        else:
            return render_template('error.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

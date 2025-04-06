from flask import Flask, render_template, request, redirect, url_for, send_file
from utils.downloader import download_video
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['videoUrl']
    quality = request.form['quality']
    if video_url:
        # Lade das Video herunter
        file_path = download_video(video_url, quality)
        if file_path and os.path.exists(file_path):
            # Extrahiere den Dateinamen aus dem Pfad
            file_name = os.path.basename(file_path)
            # Sende die Datei mit dem richtigen Dateinamen
            return send_file(file_path, as_attachment=True, download_name=file_name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
import subprocess
import os
import time  # Für Zeitstempel

def download_video(video_url, quality):
    # Überprüfen, ob die Qualität "best" oder "worst" ist
    if quality in ['best', 'worst']:
        format_option = quality
    else:
        # Andernfalls die Qualität als maximale Höhe verwenden
        format_option = f"bestvideo[height<={quality}]+bestaudio/best"

    # Zielverzeichnis für Downloads
    output_dir = os.path.abspath("downloads")
    os.makedirs(output_dir, exist_ok=True)

    # Füge einen Zeitstempel zum Dateinamen hinzu, um ihn eindeutig zu machen
    timestamp = int(time.time())
    output_template = os.path.join(output_dir, f"%(title)s_{timestamp}.%(ext)s")

    # Pfad zur Cookies-Datei
    cookies_file = os.path.abspath("cookies.txt")

    # Baue den yt-dlp-Befehl
    command = [
        "/usr/local/bin/yt-dlp",  # Pfad zur heruntergeladenen Binärdatei
        "--cookies", cookies_file,  # Cookies-Datei einbinden
        "-f", format_option,
        "-o", output_template,
        video_url
    ]

    # Führe den Befehl aus und fange die Ausgabe ab
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        # Extrahiere den Dateipfad aus der Ausgabe
        for line in result.stdout.splitlines():
            if "Destination:" in line:
                file_path = line.split("Destination:")[1].strip()
                print(f"Heruntergeladene Datei: {file_path}")  # Debug-Ausgabe
                return file_path
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Herunterladen des Videos: {e}")
    return None
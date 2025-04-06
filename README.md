# yt-dlp-web

This project is a simple web application that allows users to download YouTube videos using yt-dlp. The application is built with Flask and utilizes Bootstrap for a responsive design.

## Features

- Input field for YouTube video links
- Quality selection for video downloads
- User-friendly interface
- Responsive design using Bootstrap

## Structure
yt-dlp-web
├── downloads                 # Ordner für heruntergeladene Videos
│   └── *.mp4.part            # Temporäre Dateien während des Downloads
├── src
│   ├── app.py               # Hauptdatei der Flask-Anwendung
│   ├── templates
│   │   └── index.html       # Haupt-HTML-Template
│   ├── static
│   │   ├── css
│   │   │   └── styles.css   # CSS-Stile für die Webanwendung
│   │   ├── js
│   │   │   └── scripts.js   # JavaScript für die Client-seitige Funktionalität
│   │   └── favicon.ico      # Favicon für die Webanwendung
│   └── utils
│       └── downloader.py    # Hilfsfunktionen für das Herunterladen von Videos
├── requirements.txt          # Abhängigkeiten des Projekts
├── README.md                 # Projektdokumentation
└── LICENSE                   # Lizenzdatei

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/steinmannole/yt-dlp-web.git
   cd yt-dlp-web
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the YouTube video link, select the desired quality, and click the download button.

## Troubleshooting 

Maybe you need to check utils/downloader.py, if it uses the correct Path for yt-dlp (see line: 26)

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
# Speech Recognition (CSC 309 Demo)

This project is a browser-based speech-to-text demo built with FastAPI, OpenAI Whisper, and a simple HTML frontend. It allows a user to either record audio directly in the browser or upload an audio file, send that audio to a Python backend, and receive a transcription result. The project also includes MFCC feature extraction for audio analysis and academic explanation.

## Overview

The application provides two main capabilities:

- Speech transcription using Whisper
- Audio feature extraction using MFCCs

The backend is implemented in FastAPI and serves both the API and the browser frontend. The frontend uses browser audio APIs to record from the microphone, submit audio to the backend, and display the resulting transcript.

## Features

- Browser-based microphone recording
- Audio file upload for transcription
- Speech-to-text transcription with Whisper
- MFCC feature extraction endpoint
- FastAPI Swagger documentation
- Simple UI for live demo use
- Windows-friendly FFmpeg support in the backend

## Tech Stack

- Python
- FastAPI
- Uvicorn
- OpenAI Whisper
- Librosa
- SoundDevice
- HTML
- CSS
- JavaScript
- FFmpeg

## Project Structure

```text
SpeechRecognition/
├── app.py
├── README.md
├── requirements.txt
├── speech_recognition_project_plan.md
├── audio/
│   └── record_audio.py
├── frontend/
│   └── index.html
├── model/
│   └── whisper_model.py
└── utils/
    └── feature_extraction.py
```

## File Guide

- `app.py`: Main FastAPI application. Defines routes, serves static files, stores uploads, and returns transcription or MFCC results.
- `frontend/index.html`: Browser UI for recording audio, uploading files, and showing results.
- `model/whisper_model.py`: Loads the Whisper model and performs audio transcription.
- `utils/feature_extraction.py`: Extracts MFCC audio features.
- `audio/record_audio.py`: Small script for recording sample audio directly from Python.
- `requirements.txt`: Python packages needed to run the project.

## Requirements

Before running the project, make sure you have:

- Python 3.8 or newer
- FFmpeg installed
- Internet access on first model download if Whisper has not yet been cached locally

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/maureenokolie440-oss/Speech_Recognition.git
cd SpeechRecognition
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Whisper depends on FFmpeg to decode audio files.

Windows with Winget:

```powershell
winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements
```

macOS with Homebrew:

```bash
brew install ffmpeg
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
```

## Running the Application

Run the backend server:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

For development with auto-reload:

```bash
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

After startup, open:

- Frontend UI: `http://127.0.0.1:8000/frontend/index.html`
- Swagger docs: `http://127.0.0.1:8000/docs`
- Root endpoint: `http://127.0.0.1:8000/`

## How to Use the Demo

### Record from the browser

1. Open the frontend page.
2. Click `Record`.
3. Allow microphone access if prompted.
4. Speak clearly.
5. Click `Stop`.
6. Click `Transcribe` if the browser does not auto-submit.
7. Wait for the transcript to appear.

### Upload an audio file

1. Open the frontend page.
2. Click `Choose file`.
3. Select an audio file such as `.wav`, `.mp3`, `.ogg`, `.m4a`, or `.webm`.
4. Click `Transcribe`.
5. Wait for the returned transcript.

## API Endpoints

### `GET /`

Returns a welcome message.

Example response:

```json
{
  "message": "Welcome to the CSC 309 Speech Recognition API. Use /transcribe/ or /extract-features/ endpoints."
}
```

### `POST /transcribe/`

Uploads an audio file and returns a transcription.

Form field:

- `file`: audio file

Successful response:

```json
{
  "transcript": "This is a sample transcription."
}
```

Error response example:

```json
{
  "error": "Detailed backend error message"
}
```

### `POST /extract-features/`

Uploads an audio file and returns MFCC features.

Form field:

- `file`: audio file

Response shape:

```json
{
  "mfcc": [[1.23, 4.56], [7.89, 0.12]]
}
```

## How the Pipeline Works

1. The user records or uploads audio from the browser.
2. The frontend sends the file to the backend.
3. The backend stores the uploaded file in the `audio` folder.
4. Whisper processes the file and generates a transcript.
5. The API returns JSON to the frontend.
6. The frontend displays the transcript in the browser.

## Whisper Model Notes

The current implementation uses Whisper `tiny` for speed. This is a practical choice for classroom demos and low-resource systems, but it is less accurate than larger models.

If you want better accuracy, update the model loader in `model/whisper_model.py` from:

```python
model = whisper.load_model("tiny")
```

to a larger model such as:

```python
model = whisper.load_model("base")
```

## Recording Audio with Python

The repo includes a standalone recording script:

```bash
python audio/record_audio.py
```

This script:

- records for 5 seconds
- uses a 16 kHz sample rate
- saves output as `sample.wav`

You can upload that recorded file through the frontend afterward.

## Troubleshooting

### `Error during transcription`

Possible causes:

- FFmpeg is not installed
- FFmpeg is not available in the running shell
- the uploaded file is invalid or corrupted

Check FFmpeg:

```bash
ffmpeg -version
```

If FFmpeg is installed but not found, restart the terminal and server.

### Microphone recording does not work

Possible causes:

- microphone permission denied
- wrong recording device selected
- browser restriction or blocked permission

Fixes:

- allow microphone access in the browser
- reload the page after granting permission
- test using `127.0.0.1` or `localhost`

### First transcription is slow

This is normal when Whisper is downloading or initializing the model for the first time.

### Port 8000 is already in use

If Uvicorn reports that port `8000` is busy, stop the existing process or use another port.

Example:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8001
```

### Transcript text overflows the UI

The frontend has been updated to wrap long transcript text and allow scrolling inside the transcript box.

## Academic Relevance

This project is appropriate for coursework or live presentation in AI and speech processing because it demonstrates:

- transformer-based speech recognition
- audio preprocessing and file upload
- MFCC extraction for signal-feature analysis
- a full-stack workflow from user input to ML inference output

## Limitations

- The `tiny` model favors speed over accuracy.
- Very noisy recordings may produce weak results.
- Longer recordings take more time to process.
- Uploaded files are stored locally in the `audio` directory.

## Future Improvements

- Add language selection
- Add support for longer streaming sessions
- Save transcript history in a database
- Add transcript export
- Add speaker separation
- Add authentication and user history

## License

This project is intended for educational use.

## Author

Prepared as a CSC 309 speech recognition demonstration project.

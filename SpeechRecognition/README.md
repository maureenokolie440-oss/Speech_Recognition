# Speech Recognition (CSC 309 Demo)

A FastAPI-based web application for real-time speech-to-text transcription using OpenAI's Whisper model. Record audio directly from your browser or upload audio files to get instant transcriptions.

## Features

- 🎤 **Real-time Recording** — Record audio directly in the browser
- 📁 **File Upload** — Support for all audio formats (WAV, MP3, OGG, WEBM, etc.)
- 🤖 **Whisper AI** — Powered by OpenAI's Whisper tiny model for fast transcription
- 🎨 **Modern UI** — Clean, responsive web interface with real-time feedback
- 📊 **Audio Features** — Extract MFCC (Mel-Frequency Cepstral Coefficients) for audio analysis

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **ML Model**: OpenAI Whisper (tiny model for speed)
- **Audio Processing**: librosa, sounddevice
- **Server**: Uvicorn

## Requirements

- Python 3.8+
- FFmpeg (for audio decoding)
- Dependencies listed in `requirements.txt`

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/maureenokolie440-oss/Speech_Recognition.git
cd Speech_Recognition
```

### 2. Install FFmpeg

**Windows (using Winget):**
```bash
winget install --id Gyan.FFmpeg -e
```

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

### 3. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The server will start at `http://127.0.0.1:8000`

### Access the Demo UI

Open your browser and navigate to:
```
http://127.0.0.1:8000/frontend/index.html
```

### API Documentation

Interactive Swagger API docs available at:
```
http://127.0.0.1:8000/docs
```

## Project Structure

```
Speech_Recognition/
├── app.py                      # FastAPI application with ffmpeg path configuration
├── frontend/
│   └── index.html             # Web UI with recording and upload
├── model/
│   └── whisper_model.py       # Whisper transcription model
├── utils/
│   └── feature_extraction.py  # Audio MFCC feature extraction
├── audio/                      # Uploaded/recorded audio files directory
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## API Endpoints

### Transcribe Audio File

**POST** `/transcribe/`

Upload an audio file and get a text transcript.

**Request:**
- `file`: Audio file (any format supported by ffmpeg)

**Response:**
```json
{
  "transcript": "Okay, so this is a test demo of the speech recognition for CS309 demo."
}
```

### Extract Audio Features

**POST** `/extract-features/`

Extract MFCC features from an audio file for analysis.

**Request:**
- `file`: Audio file

**Response:**
```json
{
  "mfcc": [[...], [...], ...]
}
```

## How It Works

1. **Recording**: Use the browser's Web Audio API to capture microphone input
2. **Upload**: Send audio to the FastAPI backend as multipart form data
3. **Processing**: FFmpeg decodes the audio file
4. **Transcription**: Whisper model converts audio to text
5. **Response**: Transcribed text is displayed in the browser

## Performance Notes

- **First Run**: Whisper model downloads on first use (~1.4 GB for tiny model)
- **Processing Time**: 5-15 seconds per minute of audio depending on hardware
- **Model**: Using the "tiny" model for speed. Switch to "base" in `model/whisper_model.py` for better accuracy

## Troubleshooting

### "Error during transcription"

**Cause**: FFmpeg not found or audio decoding failed  
**Solution**: Ensure FFmpeg is installed and on your PATH. Verify with: `ffmpeg -version`

### Browser can't access microphone

**Cause**: Microphone permission not granted  
**Solution**: Check browser permission settings. HTTPS is required for secure contexts (localhost works fine locally).

### Model download takes too long

**Cause**: Large model file download  
**Solution**: The model is cached after first download. Subsequent transcriptions will be faster.

## Academic Notes (CSC 309)

- MFCC extraction included via the `/extract-features/` endpoint for signal processing analysis
- Whisper model demonstrates state-of-the-art speech recognition using transformers
- Project covers full ML pipeline: data collection → processing → inference

## Future Improvements

- [ ] Support for batch file processing
- [ ] Multiple language support
- [ ] Speaker diarization
- [ ] Real-time streaming transcription
- [ ] Database to store transcription history
- [ ] User authentication and usage tracking

## License

Educational project for CSC 309 course.

## Author

Created for CSC 309 (Artificial Intelligence) course demonstration.

---

**Questions or Issues?** Feel free to open an issue on GitHub!

---

**Prepared for CSC 309 – Artificial Intelligence**

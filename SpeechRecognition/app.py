from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from model.whisper_model import transcribe_audio
from utils.feature_extraction import extract_mfcc
import shutil
import os

# Ensure ffmpeg is on the PATH (winget installs here on Windows)
_ffmpeg_bin = r"C:\Users\USER\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"
if os.path.isdir(_ffmpeg_bin) and _ffmpeg_bin not in os.environ.get("PATH", ""):
    os.environ["PATH"] = _ffmpeg_bin + os.pathsep + os.environ.get("PATH", "")



app = FastAPI()

# Serve static frontend files at /frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Root endpoint for welcome message
@app.get("/")
def root():
    return {"message": "Welcome to the CSC 309 Speech Recognition API. Use /transcribe/ or /extract-features/ endpoints."}

UPLOAD_DIR = "audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe/")
def transcribe(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        transcript = transcribe_audio(file_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    return {"transcript": transcript}

@app.post("/extract-features/")
def extract_features(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    mfccs = extract_mfcc(file_path)
    return JSONResponse(content={"mfcc": mfccs.tolist()})

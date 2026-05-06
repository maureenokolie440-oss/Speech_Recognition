import whisper

# Load the Whisper model once (tiny for speed, change to 'base' for better accuracy)
model = whisper.load_model("tiny")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

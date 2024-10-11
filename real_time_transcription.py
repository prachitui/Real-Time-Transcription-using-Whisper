import whisper
import sounddevice as sd
import numpy as np
import torch
from scipy.io.wavfile import write

# Load the Whisper model (choose 'base', 'small', or 'large' based on performance needs)
model = whisper.load_model("base")

# Audio settings
samplerate = 16000  # Whisper expects 16kHz mono input
duration = 5  # seconds per chunk


# Function to capture and transcribe audio in real-time
def transcribe_audio(indata): #extra, frames, time, status):
    audio_chunk = np.squeeze(indata)

    # Save audio chunk temporarily
    write("temp_audio.wav", samplerate, audio_chunk)

    # Load the audio and transcribe
    result = model.transcribe("temp_audio.wav", language="en")
    print(result['text'])


# Stream audio and transcribe in real-time
with sd.InputStream(callback=transcribe_audio, channels=1, samplerate=samplerate):
    print("Recording... Press Ctrl+C to stop.")
    sd.sleep(int(duration * 1000 * 60))  # 60 minutes runtime

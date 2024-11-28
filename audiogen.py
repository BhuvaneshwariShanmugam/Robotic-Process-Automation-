import sounddevice as sd
import numpy as np
from scipy.io import wavfile  # Correct import for wavfile

def record_audio(filename="record.wav", duration=5, fs=44100, channels=1):
    print(f"Recording for {duration} seconds...")
    # Record audio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()  # Wait for the recording to finish
    print("Recording finished!")
    
    # Convert the audio to 16-bit PCM format
    recording = (recording * 32767).astype(np.int16)
    
    # Save the recording using wavfile.write from scipy.io
    wavfile.write(filename, fs, recording)
    print(f"Audio file saved as '{filename}'")
    
record_audio(filename="audio.wav", duration=5)
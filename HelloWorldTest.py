import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "mic_recording.wav"

audio = pyaudio.PyAudio()

# Open the microphone stream
stream = audio.open(format = FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNK)

print("Recording...")
frames = []

for _ in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


print("Recording finished.")

# Stop & close stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save to WAV file

with wave.open(OUTPUT_FILENAME, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b"".join(frames))

print(f"Saved as {OUTPUT_FILENAME}")



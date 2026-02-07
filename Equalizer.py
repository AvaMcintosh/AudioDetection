import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter

# --- Helper functions for bandpass filters ---
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# --- Load WAV file ---
input_file = "input.wav"
output_file = "output_eq.wav"
data, fs = sf.read(input_file)  # data = waveform, fs = sample rate

# --- Define bands in Hz ---
bands = {
    "low": (20, 300),
    "mid": (300, 4000),
    "high": (4000, fs//2)
}

# --- Set gains for each band (linear multiplier) ---
gains = {
    "low": 1.5,   # boost bass
    "mid": 1.0,   # keep mids same
    "high": 0.8   # cut treble
}

# --- Apply band filters and gains ---
output = np.zeros_like(data)
for band, (low, high) in bands.items():
    filtered = bandpass_filter(data, low, high, fs)
    output += filtered * gains[band]

# --- Normalize to prevent clipping ---
max_val = np.max(np.abs(output))
if max_val > 1.0:
    output /= max_val

# --- Save output ---
sf.write(output_file, output, fs)
print(f"Equalized audio saved as {output_file}")

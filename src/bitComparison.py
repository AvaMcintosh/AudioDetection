import bitstring
from bitstring import BitArray

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.io import wavfile
from scipy.signal import correlate
from scipy.fft import fft, ifft

def create_spectrogram_2(file_path):
    fs, x = wavfile.read(file_path)

    # 1. Handle stereo to mono conversion FIRST
    if x.ndim > 1:
        x = x.mean(axis=1)

    # 2. Store the original length of the audio signal
    n = len(x) 

    # 3. Compute the Real FFT
    # Don't overwrite 'x' so you don't lose the original length reference
    x_transformed = np.fft.rfft(x)
    mag = np.abs(x_transformed)
    print(f"MAG: {mag}")
    # 4. Compute frequencies using the ORIGINAL length 'n'
    freqs = np.fft.rfftfreq(n, 1/fs)
    print(f"FREQ: {freqs}")

    # Now shapes will match: (n/2 + 1,) and (n/2 + 1,)
    plt.figure(figsize=(10, 4))
    plt.plot(freqs, mag)
    plt.title(f'Spectrogram: {file_path}')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.show()


def create_spectrogram(file_path):
    # 1. Load the audio file
    # y is the audio time series, sr is the sampling rate
    # y, sr = librosa.load(file_path)
    fs, x = wavfile.read(file_path)

    # 2. Compute the Short-Time Fourier Transform (STFT)
    # We take the absolute value to get the magnitude
    #stft = np.abs(librosa.stft(y))
    print(x)
    stft = fft(x)
    
    # 3. Convert amplitude to decibels (log scale)
    # This makes the visualization much easier for humans to read
    db_spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

    
    #4. Create the plot
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(db_spectrogram, sr=sr, x_axis='time', y_axis='hz', cmap='magma')
    
    # Add a color bar and labels
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram: {file_path}')
    plt.tight_layout()
    plt.show()

    normSpec = librosa.util.normalize(db_spectrogram, axis=None)


    return normSpec


# base = BitArray(bytes=open('src/HELLO.wav', 'rb').read())
##print(base.bin)

# carHonk = BitArray(bytes=open('src/CarHonk1.wav', 'rb').read())

# chunk_size = 50000



# for i in range(0, len(base), chunk_size):
#     # Get the chunk from index i to i + chunk_size
#     chunk = base[i:i + chunk_size]
    
#     #print(f"Processing chunk starting at index {i}: {chunk}")

#     if(chunk.bin in carHonk.bin):{
#         print("HONK")
#     }
#     else: {
#         print("Nothing")
#     }

print('file1')
spectrogram1 = create_spectrogram_2('src/loudHonk.wav')

# print('file2')
spectrogram2 = create_spectrogram_2('src/CarHonk1.wav')


# corr = scipy.signal.correlate2d(spectrogram1, spectrogram2, mode="valid")
# similarity = corr.min()

# print("Similarity score:", similarity)
    # Process the chunk
    

##test = base[:20]

##print(base.bin)


## take in input
## every (Number of bits) check for comparison to car honking bitwise

## if there is over a 90% match say true


#carHonk = BitArray(bytes=open('src/CarHonk1.wav', 'rb').read())
##print(carHonk.bin)
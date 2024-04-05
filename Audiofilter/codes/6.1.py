import soundfile as sf
from scipy import signal, fft
import numpy as np
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    # Pad the input signal to match the length required for filtering
    padlen = max(len(a), len(b)) * 3
    input_signal_padded = np.pad(input_signal, (padlen, padlen), mode='edge')
    
    # Apply forward and backward filtering
    filtered_signal = signal.lfilter(b, a, input_signal_padded)
    filtered_signal = np.flip(filtered_signal)
    filtered_signal = signal.lfilter(b, a, filtered_signal)
    filtered_signal = np.flip(filtered_signal)
    
    # Trim the padded sections
    filtered_signal_trimmed = filtered_signal[padlen:-padlen]
    
    return filtered_signal_trimmed

# Read .wav file 
input_signal, fs = sf.read('kkaudio_2.wav')
print(len(input_signal))
np.savetxt("in.txt", input_signal)

if len(input_signal.shape) > 1:
    input_signal = input_signal[:, 0]
# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 
cutoff_freq = 4000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter
output_signal_builtin = signal.filtfilt(b, a, input_signal)

# Filter the input signal using custom function
output_signal_custom = myfiltfilt(b, a, input_signal)

# Verify outputs by plotting
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal_builtin[1000:10000], 'b.', label='Output by built-in function')
plt.plot(x_plt[1000:10000], output_signal_custom[1000:10000], 'r.', label='Output by custom function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig('output_verf.png')


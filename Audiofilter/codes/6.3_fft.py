import os
import ctypes
import numpy as np

# Get the current working directory
current_dir = os.getcwd()

# Construct the path to the shared library
lib_path = os.path.join(current_dir, 'fft.so')

# Load the shared library
lib = ctypes.CDLL(lib_path)

# Define the return type and argument types for the FFT function
lib.myfft.restype = ctypes.POINTER(ctypes.c_double * 2)
lib.myfft.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double * 2)]

# Define the input data
input_data = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
n = len(input_data)

# Prepare the input data (real part only)
input_data_c = (ctypes.c_double * n)(*input_data)

# Call the FFT function
result = lib.myfft(n, input_data_c)

# Extract the real and imaginary parts from the result
result_np = np.array(result.contents).reshape(-1, 2)

# Print the FFT result
print("FFT result:")
for i, (real, imag) in enumerate(result_np):
    print(f"{real:.2f} + {imag:.2f}i")


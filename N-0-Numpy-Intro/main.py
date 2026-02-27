import numpy as np

# Create a noisy signal using numpy
time = np.linspace(0, 10, 1000)        # 1000 points from 0 to 10s
signal = np.sin(2*np.pi*5*time)        # 5 Hz vibration

# Check the type
print(f"Time and signal are of type {type(time)} and {type(signal)}")

# Add a normally distributed random noise to the signal
noisy_signal = signal + 0.2*np.random.randn(1000)

# Inspect the shape
print(f"Shape of the signal is {noisy_signal.shape}")

# Compute average and standard deviation using numpy
print(f"The mean of the signal is {np.mean(noisy_signal)}")
print(f"The standard deviation of the signal is {np.std(noisy_signal)}")

# Save the signal to file
np.savetxt('signal.csv', noisy_signal, delimiter='\n')
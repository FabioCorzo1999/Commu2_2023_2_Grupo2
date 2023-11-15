import numpy as np
from gnuradio import gr
import math

class e_RF_VCO_ff(gr.sync_block):  
    """
    This block is an RF Voltage-Controlled Oscillator (RF VCO).
    
    Parameters:
    - fc (float): Center frequency of the VCO.
    - samp_rate (float): Sampling rate.
    
    The block takes in two input signals, A (Amplitude) and Q (Quadrature),
    and produces an RF-modulated output signal.

    The block modulates the amplitude (A) with a cosine waveform, where the
    frequency is determined by the center frequency (fc). The phase of the cosine
    is controlled by the quadrature (Q).

    The output signal is given by: y = A * cos(2 * pi * fc * n / samp_rate + Q),
    where n is the sample index.
    """

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m = 0

    def work(self, input_items, output_items):
        # Extract input signals
        A = input_items[0]
        Q = input_items[1]
        
        # Extract output signal
        y = output_items[0]
        
        # Number of samples
        N = len(A)
        
        # Sample index
        n = np.linspace(self.n_m, self.n_m + N - 1, N)
        self.n_m += N
        
        # Perform modulation: y = A * cos(2 * pi * fc * n / samp_rate + Q)
        y[:] = A * np.cos(2 * math.pi * self.fc * n / self.samp_rate + Q)
        
        return len(output_items[0])


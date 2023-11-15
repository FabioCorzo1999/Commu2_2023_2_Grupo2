import numpy as np
from gnuradio import gr

class e_CE_VCO_fc(gr.sync_block):  
    """
    This block is a Complex Envelope Voltage-Controlled Oscillator (CE VCO)
    and works as follows: It takes in two input signals, A (Amplitude) and Q (Quadrature),
    and produces a complex output signal y = A * exp(1j * Q).

    Parameters:
    - A (input_items[0]): Input signal representing the amplitude.
    - Q (input_items[1]): Input signal representing the quadrature.
    - y (output_items[0]): Complex output signal.

    The block performs the modulation operation by multiplying the amplitude (A)
    with the complex exponential of the quadrature (Q), producing the modulated signal.
    """

    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        # Extract input signals
        A = input_items[0]
        Q = input_items[1]
        
        # Extract output signal
        y = output_items[0]
        
        # Number of samples
        N = len(A)
        
        # Perform modulation: y = A * exp(1j * Q)
        y[:] = A * np.exp(1j * Q)
        
        return len(output_items[0])


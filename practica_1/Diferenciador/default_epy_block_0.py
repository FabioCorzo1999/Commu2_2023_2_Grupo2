"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):  # Solo argumentos predeterminados aquí
        gr.sync_block.__init__(
            self,
            name='Diferenciador',  # Aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32],
        )
        self.acum_anterior = 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada.
        y0 = output_items[0]  # Señal acumulada diferencial
        N = len(x)
        diff = np.cumsum(x) - self.acum_anterior
        self.acum_anterior = diff[N - 1]
        y0[:] = diff
        return len(y0)
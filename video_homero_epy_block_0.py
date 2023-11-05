"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """este bloque fue creado por carlos viendo un video del profesor homero"""
        gr.sync_block.__init__(
            self,
            name='VCO complex',   # will show up in GRC
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
    	Q=input_items[0]
    	A=input_items[1]
    	Sec=output_items[0]
    	Sec[:]=A*np.exp(1.j*Q)
    	return len(Sec)

import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: ….."""
    """ En este bloque manejamos una señal modulada para convertirla en un aseñal RF
        Donde a partir de una señal y una constante se puede hacer esta, la señal que es un señal modulada 
        y la contante que me va representar el desfase que queremos que tenga la señal RF.

        La variable A es la señal de entrada (señal modulda )
        Q que es mi contante que significara el desfase de una señal RF 
        N es la constante que me dira el rango nuestra señal modulada teniendo en cuenta que esta vive aumentando 

        n es el vector de teneindo en cuenta que inicia en 0 y termina en N-1 con un numero de muestras de N
        y el numero de muestras va aumentando a medida que aumenta N
        una vez esto me retorna el vector de referencia de la modulacion."""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0] #señal de entrada modulada
        Q=input_items[1] #Descafe se la señal de salida
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(y)



#!/usr/bin/python
    
import sys, serial
import dmm
import ps
 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from time import sleep

instr = ps.psinit("USB0::0x0AAD::0x0135::035375054::INSTR")
ps.pssel(instr,1)

s = serial.Serial('COM4', 9600)
dmm.command(s, 'ADC')
dmm.reset(s)

V_in = np.linspace(1, 20, 100)
output = open('../dati/lamp.txt', 'w')

fig, ax = plt.subplots()
ax.set_xlabel('$V_{in}$')
ax.set_ylabel('corrente i$I$')

I_a = np.array([])
eI_a = np.array([])
V_a = np.array([]) 

for V in V_in:
    instr.write(f'APPLY {V},0.1')
    sleep(0.5)
    I, sigma_I = dmm.dmmread(s)
    out = f'{V} {I} {sigma_I}\n'
    output.write(out)
    print(out)
    
    V_a = np.append(V_a, V)
    I_a = np.append(I_a, I)
    eI_a = np.append(eI_a, sigma_I)

    ax.errorbar(V_a, I_a, yerr=eI_a, color='k')
    plt.gcf().canvas.flush_events()
    fig.show()




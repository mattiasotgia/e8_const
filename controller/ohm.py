import sys, serial
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

import numpy as np
import dmm, ps


if __name__ == '__main__':
    s4 = serial.Serial('COM4', 9600); dmm.reset(s4)
    dmm.command(s4, 'OHMS')
    dmm.reset(s4)
    fig, ax = plt.subplots()
    
    R = np.array([])
    eR = np.array([])
    
    ax.set_xlabel('$R_{light}$')
    ax.set_ylabel('Events'); data = open('../dati/ohm.txt', 'w')

    for _ in range(10_000):
        tmp_R, tmp_eR = dmm.dmmread(s4)
        R = np.append(R, tmp_R)
        eR = np.append(eR, tmp_eR); data.write(f'{tmp_R} {tmp_eR}')
        
        ax.clear()
        ax.hist(R, weights=eR, histtype='step')
        plt.gcf().canvas.flush_events()
        fig.show()

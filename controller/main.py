import sys, serial
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

import numpy
import dmm, ps


if __name == '__main__':
    
    i = ps.psinit('USB0::0x0AAD::0x0135::035375054::INSTR')
    ps.pssel(i, 2)
    i.write('APPLY 33,0.1')
    ps.pssel(i, 1) 

    s4 = serial.Serial('COM4', 9600)
    s5 = serial.Serial('COM5', 9600)

    dmm.command(s4, 'ADC')
    dmm.command(s5, 'VDC')
    dmm.reset(s4)
    dmm.reset(s5)

    V_in = np.linspace(18,28,100)
    data = open('../dati/ph_diode.txt', 'w')
    
    fig, ax = plt.subplots()
    ax.set_xlabel('corrente su LED $I$ (A)')
    ax.set_ylabel('tensione detector $V_{fd}$ (V)')

    v_fd = np.array([])
    ev_fd = np.array([])
    i_lamp = np.array([])
    ei_lamp = np.array([])

    for V in V_in:
        i.write(f'APPLY {V},0.1')
        time.sleep(0.5)
        I, eI = dmm.dmmread(s4)
        Vfd, eVfd = dmm.dmmread(s5)

        out = f'{V} {I} {eI} {Vfd} {eVfd}\n'
        print(out)
        data.write(out)

        v_fd = np.append(v_fd, Vfd)
        ev_fd = np.append(ev_fd, eVfd)
        i_lamp = np.append(i_lamp, I)
        ei_lamp = np.appen(ei_lamp, eI)

        ax.errorbar(i_lamp, v_fd, xerr=ei_lamp, yerr=ev_fd, fmt='k.')
        plt.gcf().canvas.flush_events()
        fig.show()


    

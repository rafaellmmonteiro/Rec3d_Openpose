# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:18:12 2021

@author: Rafael Monteiro
"""
import pdb
import shutil
import os
from os import walk
import glob
import numpy as np
import scipy as sp
from scipy import interpolate
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from numpy.linalg import inv
from iteration_utilities import deepflatten

def filtro(dat, fc=59, fs=1000, filtorder=4, typefilt='low'):
    import numpy as np
    from scipy import signal
    
    nl, nc = dat.shape
    # fc=59  # Cut-off frequency of the filter
    w = fc/(fs/2)  # Normalize the frequency
    b, a = signal.butter(filtorder, w, typefilt)
    
    datf = np.zeros([nl, nc], dtype=float)
    for i in range(nc):
        datf[:,i] = signal.filtfilt(b, a, dat[:,i])
   
    return datf

def run(path, path_saida):

    dat = np.loadtxt(path)   #ler arquivo
    dat1 = dat
    dat = dat[:-1, 1:51]
    datf = filtro(dat, fc=7, fs=30, filtorder=4, typefilt='low')  #inserir características do filtro: fc = frequência de corte e fs = frequência de aquisição
    save = np.loadtxt(path)
    save = save[:-1,:51]
    save[:,1:] = datf
    fmt = '%d', '%f','%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f'
    np.savetxt(path_saida, save, fmt=fmt)
    print( 'filtrado com sucesso')

    return()

path = 'C:\\Users\\rafae\\OneDrive\\Documentos\\Mestrado\\reconstrucao_3d_pose\\Salto_vertical\\Reconstrucao_3d\\for3d\\c1\\dvideow_people_0.dat'
path_saida = 'C:\\Users\\rafae\\OneDrive\\Documentos\\Mestrado\\reconstrucao_3d_pose\\Salto_vertical\\Reconstrucao_3d\\for3d\\c1\\dvideow_people_0f.dat'
run(path, path_saida)


path = 'C:\\Users\\rafae\\OneDrive\\Documentos\\Mestrado\\reconstrucao_3d_pose\\Salto_vertical\\Reconstrucao_3d\\for3d\\c2\\dvideow_people_0.dat'
path_saida = 'C:\\Users\\rafae\\OneDrive\\Documentos\\Mestrado\\reconstrucao_3d_pose\\Salto_vertical\\Reconstrucao_3d\\for3d\\c2\\dvideow_people_0f.dat'
run(path, path_saida)


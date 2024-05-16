import os
import sys
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


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


#try:
# os.system('conda install -c conda-forge ezc3d')
## If you already have the ezc3d module installed just continue
#except:
 #sys.exit(print('Restart the procedure after installation to convert the file to .c3d.'))

import ezc3d

# lend arquivo e criando c3d vazio
c3d = ezc3d.c3d()

path = 'C:/Users/rafae/OneDrive/Documentos\Mestrado/reconstrucao_3d_pose/Salto_vertical/Reconstrucao_3d/working3d/arq3d_0.3d'
dat = open(path,'r+',)
dat = pd.read_csv(dat, sep= ' ',header=None)
dat = dat.to_numpy()
tdat= len(dat)
dat=dat[:tdat-1,:]
dat = filtro(dat, fc=3, fs=120, filtorder=4, typefilt='low')
dat = dat*1000


# escrevendo o c3d
c3d['parameters']['POINT']['RATE']['value'] = [tdat]
c3d['parameters']['POINT']['LABELS']['value'] = ('Nose', 'Neck', 'Right_Shoulder', 'Right_Elbow',
                                                 'Right_Fist','Left_Shoulder','Left_Elbow','Left_Fist','Pubis',
                                                 'Right_Hip','Right_Knee','Right_Ankle','Left_Hip','Left_Knee',
                                                 'Left_Ankle', 'Right_Eye', 'Left_Eye', 'Right_Ear', 'Left_Ear',
                                                 'Left_Hallux','Left_V_Metatarsal','Left_Calcaneus',
                                                 'Right_Hallux','Right_V_Metatarsal','Right_Calcaneus')

c3d['data']['points'] = np.random.rand(4, 25, tdat-1)
cont=cont1=cont2=0
col=0
col1=1
col2=2
while (cont<25):
    c3d['data']['points'][0, cont, :] = dat[:,col]
    cont=cont+1
    col=col+3
while (cont1<25):
    c3d['data']['points'][1, cont1, :] = dat[:,col1]
    cont1=cont1+1
    col1=col1+3
while (cont2<25):
    c3d['data']['points'][2, cont2, :] = dat[:,col2]
    cont2=cont2+1
    col2=col2+3

c3d.write(path[:-3]+".c3d")

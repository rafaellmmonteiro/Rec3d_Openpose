Para rodar a reconstrução 3D utilizando o OpenPose. 

Inicialmente fazer o print dos calibradores e inserir dentro da pasta /snap_calib/c1 e /snap_calib/c2.\n
Rodar o código makecalib_dat.py
Fazer o arquivo refcal.ref com as coordenadas reais dos pontos do calibrador dentro da pasta /info_calib
Rodar código make_dlt.py
Colocar .dat nas pastas /for3d/c1 e /for3d/c2
Rodar código make_rec3d.py

Os resultados vão aparecer na pasta /working3d

Para converter o arquivo .3d para .c3d e vizualizar no mokka rodar o coord2c3d.py

Para filtrar os dados, calcular o centro de massa e converter para .c3d rodar os códigos: filtdats.py, CM2Dopenposedats.py e coord2c3d_cm.py. ****Necessário ajustes****

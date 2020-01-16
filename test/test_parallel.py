#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:51:23 2020

@author: heleneternisiendeboiville
"""

from time import time, sleep 
import museotoolbox  as mtb
from museotoolbox import datasets
from joblib import Parallel, delayed, cpu_count

"""

Test : 
    In this script four techniques are measured
   to assess the efficiency of Joblib in RasterMath    

"""

#---------------Jeu de données utilité------------------------
raster,vector = mtb.datasets.load_historical_data()
rM = mtb.processing.RasterMath(raster,verbose=False)

#--------Création d'un liste des blocks de l'image------------

blocks = [rM.get_block(i) for i in range(rM.n_blocks)]

#----------Définition de la fonction utilisée-----------------

def fun(X):
    for l in range (X.shape[0]):
        X[l,...]
    return X
    
#----------Première technique : fonction simple---------------
     
t1 = time()
res_blocks = []
for i in blocks:
    res_blocks.append(fun(i))
print ('Simple function time : ' +str(time()-t1)+ ' \n')


#----------Deuxième technique : fonction simple---------------


t0= time() 
B = Parallel(n_jobs= 4)(delayed(fun)(i) for i in blocks)   
print ('Simple function time + parallel : '+ str(time()-t0)+ ' \n')


#--------Troisème technique : fonction Run de MTB-------------

rM.add_function(fun, out_image='/Users/heleneternisiendeboiville/Desktop/SITS/test2.tif')
t0=time()
rM.run()
print ('time of the run  : '+ str(time()-t0)+ ' \n')


#---Quatrième technique : fonction run modifiée (Parallel)----

rM.add_function(fun, out_image='/Users/heleneternisiendeboiville/Desktop/SITS/test.tif')
t0=time()
rM.run_Parallel_short ()
print ('time of the run with parallel but without writing : '+ str(time()-t0)+ ' \n')




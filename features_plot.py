import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import changing_type, plot_features

#Days of the datas
autoclass_array=np.load('autoclass_array.npy',allow_pickle=True)
day=[]
for string in autoclass_array:
    day.append(string[5]+string[6]+'/'+string[7]+string[8])
    


volume=np.load('volume.npy',allow_pickle=True)     
area=np.load('area.npy',allow_pickle=True)



[df_volume,L]=changing_type(volume,day)
plot_features(day,L,df_volume,'Biovolume')        
           



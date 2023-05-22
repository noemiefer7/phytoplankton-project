import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from functions import association, merge, count, average,features

#Data 
autoclass=[]
autoclass_path="2020/autoclass"
files_autoclass=os.listdir(autoclass_path) 
for filename in files_autoclass:
    autoclass.append(filename)
np.save('autoclass_array',autoclass)    
    
features=[]
features_path="2020/features"
files_features=os.listdir(features_path)
for filename in files_features:
    features.append(filename)
np.save('features_array',features)
       

volume=features('Biovolume', autoclass, features, autoclass_path, features_path)

        
    



 



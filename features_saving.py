import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from functions import association, merge, count, average_volume, average_area

#Data 
autoclass=[]
files_autoclass=os.listdir("2020/autoclass") 
for filename in files_autoclass:
    autoclass.append(filename)
np.save('autoclass_array',autoclass)    
    
features=[]
files_features=os.listdir("2020/features")
for filename in files_features:
    features.append(filename)
np.save('features_array',features)

l=len(autoclass) 


# volume=[]        
# for i in range(l):
#     [df_identification,variety_list]=association("2020/autoclass/"+autoclass[i])
#     df_merged=merge(df_identification,"2020/features/"+features[i])
#     df_count=count(variety_list,df_identification)
#     df_volume=average_volume(variety_list, df_count,df_merged)
#     volume.append(df_volume)

# # volume=np.array(volume)    
# # np.save('volume',volume)
    
# area=[]       
# for i in range(l):
#     [df_identification,variety_list]=association("2020/autoclass/"+autoclass[i])
#     df_merged=merge(df_identification,"2020/features/"+features[i])
#     df_count=count(variety_list,df_identification)
#     df_area=average_area(variety_list, df_count,df_merged)
#     area.append(df_area)

# area=np.array(area)    
# np.save('area',area)


        
    



 



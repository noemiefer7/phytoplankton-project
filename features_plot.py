import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Days of the datas
autoclass_array=np.load('autoclass_array.npy',allow_pickle=True)
day=[]
for string in autoclass_array:
    day.append(string[5]+string[6]+'/'+string[7]+string[8])
    
#lqrkg
#Putting the numpy arrays of size (18,155,2) into a dataframe of size (155,19)
volume=np.load('volume.npy',allow_pickle=True)
[N,L,C]=np.shape(volume)
count_column=1
df_volume=pd.DataFrame({'Variety':volume[0,:,0]})
for dataframe in volume:
    df_volume.insert(count_column,day[count_column-1],dataframe[:,1])
    count_column+=1
       
        
area=np.load('area.npy',allow_pickle=True)
[N,L,C]=np.shape(area)
count_column=1
df_area=pd.DataFrame({'Variety':area[0,:,0]})
for dataframe in volume:
    df_area.insert(count_column,day[count_column-1],dataframe[:,1])
    count_column+=1
 
default_x_ticks = range(len(day))       
# for i in range (L):
#     plt.figure()
#     plt.plot(default_x_ticks,df_area.iloc[i,1:19] )
#     plt.xticks(default_x_ticks, day,rotation=45)
#     plt.title('Average area of '+df_area.iloc[i,0])
#     plt.xlabel('Days')
#     plt.ylabel('Area')
#     plt.savefig('average_area/'+df_area.iloc[i,0]+'_average_area')


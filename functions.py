import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Functions 

#This function is used to associate the ID of the phytoplankton to its type
#by using the probabilities of the autoclass file
def association(autoclass):
    #File reading
    df_autoclass=pd.read_csv(autoclass,sep=',')

    #Transposition of the dataframe
    df_autoclass_trans=df_autoclass.transpose()

    #Removing of the pid row
    df1=df_autoclass_trans.drop('pid')

    #offset of the column of interest
    df2=df1.reset_index()

    #collecting of the column containing all the variety of phytoplankton
    variety=df2["index"]

    #collecting the column containing the ID
    pid_list=df_autoclass['pid']

    #in to list
    variety_list=variety.tolist()
    pid_list=pid_list.tolist()

    df_without_pid=pd.read_csv(autoclass,sep=',')
    df_without_pid.drop('pid',inplace=True, axis=1)

    kind=''

    kind_list=['']
    
    for i in range(1,len(df_without_pid.axes[0])):
        for j in range(len(df_without_pid.axes[1])-1):
            if (df_without_pid.iloc[i,j]<=1) and (df_without_pid.iloc[i,j]>0.9):
                kind=variety_list[j]
        kind_list.append(kind)  
     
    df_identification=pd.DataFrame({'ID':pid_list , 'Variety':kind_list})
    
    return df_identification,variety_list
 

#This function is used to merge the dataframe df_identification obtained with
#the association function. 
#With this function, we obtain a dataframe with each types af phytoplankton 
#with their features    
def merge(df_identification, features):
    df_features=pd.read_csv(features,sep=',')
    df_features.drop('roi_number',inplace=True,axis=1)

    df_merged=df_features.join(df_identification)
    
    pid_column=df_identification['ID']
    variety_column=df_identification['Variety']
    
    df_merged.drop('ID',inplace=True,axis=1)
    df_merged.drop('Variety',inplace=True,axis=1)
    
    df_merged.insert(0,'ID',pid_column)
    df_merged.insert(1,'Variety',variety_column)
    
    return df_merged
 
#This function is used to calculate the amount of each phytoplankton present
#in the file, this function will be use to calculate the different averages
def count (variety_list, df_identification):
    count=[]
    
    for i in variety_list:
        c=0
        for j in df_identification.iloc[:,1]:
            if i==j:
                c+=1
        count.append(c)
    df_count=pd.DataFrame({'Variety':variety_list,'Count':count})
    return df_count


#This function is used to calculate the average volume of each phytoplankton
def average(variety_list, df_count,df_merged,quantity):
    c=0
    c_variety=0
    liste=[]
    for i in df_count.iloc[:,0]:
        c_merged=0
        for j in df_merged.iloc[:,1]:
            if i==j:
                c+=df_merged.loc[c_merged,quantity]
            c_merged=c_merged+1
        if df_count.iloc[c_variety,1]!=0:
            c/=df_count.iloc[c_variety,1]  
        else:
            c=0
        liste.append(c)
        c_variety+=1
    df_average=pd.DataFrame({'Variety':variety_list, quantity:liste})
   
    return df_average


#Putting the numpy arrays of size (18,155,2) into a dataframe of size (155,19)
def changing_type (name,day):
    [N,L,C]=np.shape(name)
    count_column=1
    df_name=pd.DataFrame({'Variety':name[0,:,0]})
    for dataframe in name:
        df_name.insert(count_column,day[count_column-1],dataframe[:,1])
        count_column+=1
    return df_name,L


#This function is used to group the phytoplanktons based on one feature
def features (quantity,autoclass, features, autoclass_path,features_path):
    liste=[]  
    l=len(autoclass)       
    for i in range(l):
        [df_identification,variety_list]=association(autoclass_path+autoclass[i])
        df_merged=merge(df_identification,features_path+features[i])
        df_count=count(variety_list,df_identification)
        df_features=average(variety_list, df_count,df_merged,quantity)
        liste.append(df_features)
    return liste

def plot_features(day, L, df,quantity):
    default_x_ticks = range(len(day))     
    os.mkdir('average_'+quantity)
    for i in range (L):
        plt.figure()    
        plt.plot(default_x_ticks,df.iloc[i,1:19] )
        plt.xticks(default_x_ticks, day,rotation=45)
        plt.title('Average'+ quantity+' of '+df.iloc[i,0])
        plt.xlabel('Days')
        plt.ylabel(quantity)
        plt.savefig('average_'+quantity+'/'+df.iloc[i,0]+'_average_'+quantity)

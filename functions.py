import pandas as pd
import numpy as np

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
def average_volume(variety_list, df_count,df_merged):
    v=0
    c_variety=0
    biovolume=[]
    for i in df_count.iloc[:,0]:
        c_merged=0
        for j in df_merged.iloc[:,1]:
            if i==j:
                v+=df_merged.iloc[c_merged,3]
            
            c_merged=c_merged+1
            
        if df_count.iloc[c_variety,1]!=0:
            v/=df_count.iloc[c_variety,1]  
        else:
            v=0
            
        biovolume.append(v)
        c_variety+=1
    df_volume=pd.DataFrame({'Variety':variety_list,'Biovolume':biovolume})
   
    return df_volume

#This function is used to calculate the average area of each phytoplankton
def average_area(variety_list, df_count,df_merged):
    a=0
    c_variety=0
    area=[]
    for i in df_count.iloc[:,0]:
        c_merged=0
        for j in df_merged.iloc[:,1]:
            if i==j:
                a+=df_merged.iloc[c_merged,2]
            c_merged+=1
        if df_count.iloc[c_variety,1]!=0:
            a/=df_count.iloc[c_variety,1]
        else:
            a=0
        area.append(a)
        c_variety+=1
    df_area=pd.DataFrame({'Variety':variety_list,'Area':area})
    return df_area


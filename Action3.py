#-----Action3:统计哪个品牌的平均车型投诉最多---------
import numpy as np
import pandas as pd
df=pd.read_csv('car_complain.csv')
newdic={}
#对problem列的多个问题代号按行展开
for i in range(df.shape[1]):
    if df.columns[i]!='problem':
        newdic[df.columns[i]]=df.iloc[:,i].repeat(df['problem'].str.rstrip(',').str.split(',',).str.len()).values
    else:
        newdic[df.columns[i]]=np.concatenate(df['problem'].str.rstrip(',').str.split(',').values)
newdf=pd.DataFrame(newdic)

tongji=newdf.groupby('brand').agg({'id':'nunique','car_model':'nunique'})
#print(tongji.head())
s=tongji['id']/tongji['car_model']
NumOfProblemsPerCar=pd.Series(s).sort_values(ascending=False)
print(NumOfProblemsPerCar)
print('平均车型投诉最多的品牌为:',NumOfProblemsPerCar.index[0])

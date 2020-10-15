# import pandas as pd
# from pandas import Series
#
# se=pd.Series([1,2,3])
# se=Series([1,2,3],index=['a','b','c'])
# print(se)
# print(se[1])
# print(se[0:2])
# print(se[0:3:2])
# print(se[['a','b']])
#
# se=Series([1,2,3,4],index=['a','b','c','d'])
#
# print('a'in se)
# print('e'in se)
# print(se.values)
# #转换numpy 数组
# print(type(se.values))
#
# #判断有无空值 返回bool数组
# print(se.isnull())
# print(se.notnull())#可以结合bool切片
#
# #对多个Series进行运算
# dict={'Ohio':35000,'Oregaon':16000,'Texas':71000,'Utah':5000}
# seriesA=Series(dict)
# new_index={'Ohio','Oregaon','Texas','CA'}
# seriseB=Series(dict,index=new_index)
# aa=seriesA*seriseB
# print(aa)
#
# seriesA.name='seriesA'
# seriesA.index.name='city'
#
#
import pandas as pd
from pandas import DataFrame
data=[[1,1,1],[2,2,2],[3,3,3]]
frame=DataFrame(data,index=['N1','N2','N3'],columns=['a','b','c'])
print(frame)
data={'Num':[1,2,3],'Name':['Jack','May','Jame'],'scores':[90,93,99]}
frame_2=DataFrame(data)
frame_3=DataFrame(data,index=['a','b','c'])
print(frame_3)
data={'Beijing':{2001:2.4,2003:3},'tianjing':{2001:3.2,2002:4},'shanghai':{2000:1.0,2001:2}}
frame_4=DataFrame(data)
print(frame_4)
#行列转换
print(frame_4.T)

#对DataFrame进行索引
print(frame_4)
#只能对列进行索引
print(frame_4['Beijing'])
#花式索引
print(frame_4[['Beijing','shanghai']])
#不可以使用列索引进行切片,不推荐使用\
print(frame_4[0:2])
#.loc只能用行列的索引名称进行操作  索引 花式 切片 bool
print(frame_4.loc[[2001,2003]])
print(frame_4.loc[2001:2002])
print(frame_4.loc[2000,'shanghai'])

bo=[True,True,False,False]
print(frame_4.loc[bo])

#使用下标进行筛选，iloc[]
print('-'*20)
print(frame_4.iloc[[1,2],1])
print(frame_4.iloc[:,2])
print(frame_4.iloc[1:3])#对行筛选

print(frame_4>2)
print(frame_4[frame_4>2])

#赋值
frame_4.loc[[2002,2003],'tianjing']=100
print(frame_4)

#可以赋空值
import numpy as np
frame_4['shanghai']=np.nan
print(frame_4)

#使用Series对一列进行赋值
import pandas as pd
from pandas import Series
se=Series([88,88],index=[2000,2002])
frame_4['shanghai']=se
print(frame_4)

se=Series([1,1,1],index=['Beijing','tianjin','hangzhou'])
frame_4.loc[2000]=se
print(frame_4)

#DataFrame新增行列
frame_4['hangzhou']=[1,1,1,1]
frame_4.loc[2005]=[1,1,1,1]
print(frame_4)
#detype()查看某一列数据类型，detypes多个列数据类型
print(frame_4.dtypes)
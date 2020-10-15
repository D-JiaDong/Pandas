#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pandas import Series
'''
    Series
'''
#series的创建
arr = np.array([1,2,3])
print(arr)
#Series会自动给数值分配行索引，dtype，Series的数据类型
se = pd.Series([1,2,3])
print(se)
se = Series([1,2,3],index=list('abc'))
print(se)
data = {'a':1,'b':2,'c':3,'d':4}
se = Series(data)
print(se)

#Series对象的索引/（正常索引，切片，花式，布尔）
print(se['b'])
#使用行索引进行切片是，左右都包含
print(se['a':'b'])
#使用下标进行切片，左包含右不包含

print(se['a':'d':2])
#使用花式索引：'a','c'
print(se[['a','c']])
print(se>3)
print(se[se>3])
#使用下标索引，筛选以下四行代码的结果
print(se['b'])
print(se['a':'b'])
print(se['a':'d':2])
print(se[['a','c']])
print(se[1])
print(se[0:2])
print(se[0:4:2])
print(se[[0,2]])

#赋值
se[[0,2]]=44
print(se)
se[['a','c']]=88
print(se)

#Series矢量计算,numpy中的函数可以对Series对象进行相应操作
print(se*2)
print(np.exp(se))
print(np.sin(se))

#Series属性，index/values
#index，Series的行索引
print(se.index)
print(se.index[1])
print(se.index[1:])
#!!!!!!!!!!!!!!!!!!index不可以赋值
# se.index[1]='e'
# print(se.index)
se.index=['q','w','e','r']
print(se)
new_index = ['a','b','e','r','q']
se = Series(se,index = new_index)
print(se)

#关键字in，只是针对index
print('a' in se)
print('y' in se)
#Serise的数值，将pandas转换乘numpy的方式
print(se.values)
print(type(se.values))

#判断有无数据空值,返回布尔数组
#nan代表空值
print(se.isnull())
print(se.notnull())
print(se[se.notnull()])

#对多个Series进行运算
dict = {'Ohio':35000,'Oregon':16000,'Texas':71000,'Utah':5000}
seriesA = Series(dict)
new_index={'California','Ohio','Oregon','Texas'}
seriesB = Series(dict,index=new_index)
print(seriesA)
print(seriesB)

print(seriesA* seriesB)
aa = seriesA+seriesB
print(aa)
aa[aa.isnull()]=10000
print(aa)

seriesA.name = 'seriesA'
seriesA.index.name = 'City'
print(seriesA)


from pandas import DataFrame
data  = [[1,1,1],[2,2,2],[3,3,3]]
#index:行索引，columns列索引
frame = DataFrame(data,index=['N1','N2','N3'],columns=['a','b','c'])
print(frame)
data={'Num':[1,2,3],'name':['Jack','May','Jame'],'Scores':[90,93,99]}
frame_2 = DataFrame(data)
print(frame_2)
frame_3 = DataFrame(data,index=['a','b','c'])
print(frame_3)
data = {'Beijing':{2001:2.4,2003:3},'TianJin':{2001:3.2,2002:4},'ShangHai':{2000:1.0,2001:2}}
frame_4 = DataFrame(data)
print(frame_4)
#DataFramed对象名.T，转置（行列互换）
print(frame_4.T)

#对DataFrame进行索引
#[]只可以对列名称进行索引
print(frame_4)
print(frame_4['Beijing'])
#print(frame_4[2001])
#只筛选一列，变成Series对象
print(type(frame_4['Beijing']))
print(frame_4[['Beijing','ShangHai']])
#不可以使用列索引进行切片
#print(frame_4['Beijing':'Taijing'])
#对行索引进行切片
#不推荐使用print(frame_4[0:2])

#!!!.loc[行，列]，使用的是行列索引名称;索引，花式，切片，布尔
print(frame_4.loc[[2001,2003]])
print(frame_4.loc[2001:2002])
print(frame_4.loc[2000,'ShangHai'])
print(frame_4.loc[:,'Beijing'])
bo = [True,True,False,False]
print(frame_4.loc[bo])
#NO,print(frame_4.loc[0:])
print(frame_4.loc[2001::2])
print('--------------------------------------------')
#使用下标进行筛选，，iloc[]
print(frame_4.iloc[[1,2],1])
print(frame_4.iloc[:,2])
print(frame_4.iloc[1:3])
#布尔数组为True 返回原值，若为False则返回NaN
print(frame_4>2)
print(frame_4[frame_4>2])

print(frame_4.Beijing)

#赋值
frame_4.loc[[2002,2003],'TianJin'] = 100
print(frame_4)

#可以赋空值，np.nan
frame_4['ShangHai'] = np.nan
print(frame_4)
#使用Series对一列进行赋值
se = Series([88,88],index=[2000,2002])
frame_4['ShangHai'] = se
print(frame_4)

print(type(frame_4.loc[2000]))
se = Series([1,1,1],index = ['Beijing','TianJin','Hangzhou'])
frame_4.loc[2000] = se
print(frame_4)

#对DataFrame 新增行列
frame_4['Hangzhou'] = [1,1,1,1]
print(frame_4)
frame_4.loc[2005] = [1,1,1,1]
print(frame_4)
#dtype()查看某一列类型，dtypes多个列的数据类型
print(frame_4['Hangzhou'].dtype)
print(frame_4.dtypes)






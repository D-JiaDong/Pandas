#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
# #删除,drop()
# s1 = Series([1,2,3],index=list('abc'))
# print(s1)
# #inplace默认为False，生成视图不再原Series上进行操作
# #若想改变原Series，可将inplace = True
# #若inplace=True，drop（）该函数的返回值为None
# print(s1.drop('a',inplace=True))
# # s1.drop('a',inplace=True)
# print(s1)
# # s1 = s1.drop('a')
# #同时删除多行
# print(s1.drop(['b','c']))
# #DataFrame删除行/列
# df = DataFrame({'a':[1,1,1],'b':[2,2,2]})
# #axis=0，删除行，axis=1 删除列
# print(df)
# # df.drop(['a','b'],inplace=True,axis=1)
# # df.drop(0,inplace=True)
# print(df)
#
# #使用下标进行删除
# print(df.drop(df.index[1]))
# #columns,是列索引名
# print(df.columns)
# print(df.drop(df.columns[1],axis=1))
#
# del df['b']
# print(df)
#
# #专门删除缺失值dropna()，NaN
# data = {'a':[1,2],'b':[3,np.nan],'c':[np.nan,np.nan]}
# df = DataFrame(data)
# print(df)
# #'any',只要存在一个NaN值，则删除整行或整列
# print(df.dropna(how='any'))
# #需要整行/列都是空值才删除
# print(df.dropna(how='all',axis=1))
# #thresh=n,设置阈值，保留至少有n个非na的行或列
# print(df)
# print(df.dropna(thresh=1,axis=1))
# # #对缺失值进行赋值
# # print(df.fillna(3))
# #
# # #排序
# # df = pd.DataFrame(np.arange(12).reshape(4,3),columns=list('acd'),index=['one','two','three','four'])
# # print(df)
# # #默认是升序，由小到大，ascending = False降序
# # print(df.sort_index(ascending=False,axis=1))
# # df = pd.DataFrame([[5,3,1],[4,2,1],[5,1,5]],columns=list('abc'))
# # print(df)
# # #可以同时选用多列进行排序
# # print(df.sort_values(by=['a','b'],ascending=False))
# # #replace（）替换，to_replace 需要替换的内容，value替换的值
# # print(df.replace(to_replace=5,value = 555))
# #
# # #DataFrame属性
# # print(df.values)
# # print(df.index)
# # print(df.columns)
# # print(df)
# # df.index = ['N1','N2','N3']
# # print(df)
# # print(type(df.values))
# # df.index.name='NO'
# # df.columns.name ='NN'
# # print(df)
# # #head()返回前几行数值,默认返回5行
# # print(df.head(n=1))
# # #tail()返回后几行数据,默认返回5行
# # print(df.tail(n=2))
# # #np.nan,暂时把舍去
# # #数据统计函数
# # se = Series([2,2,5,4,0])
# # #去重
# # print(se.unique())
# # #计算Series的频数，这个函数DataFrame
# # print(se.value_counts())
# # #count,非空数值有几个,mean平均值，std标准差，
# # print(se.describe())
# #
# # df = DataFrame(np.arange(12).reshape(3,4),columns=['a','b','c','d'])
# # print(df.describe())
# # print(df.count(axis=1))
# # print(df[['b','c']].count())
# # print(df.max())
# # print(df.min())
# # print(df.sum())
# # print(df.median())
# # print(df.mean())
# # #方差
# # print(df.var())
# # #标准差
# # print(df.std())
# # print(df.cumsum(axis=1))
# # print(df.cumprod())
#
# #多个DataFrame进行运算,数据对齐
# df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
#
# df2 = pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
# print(df1)
# print(df2)
# print(df1+df2)
# #add(),sub(),mul(),div()
# print(df1.add(df2,fill_value=0))
# print(df1.mul(df2,fill_value=1))
# #广播
# se = df1.loc[0]
# print(df1)
# print(se)
# print(df1-se)


#DataFrame的合并
frame1 = DataFrame(np.arange(12).reshape(3,4),index = ['a','b','c'],columns=['N1','N2','N3','N4'])
frame2 = DataFrame(np.arange(16).reshape(4,-1),index=['a','b','c','d'],columns=['N1','N2','N3','N4'])
frame3 = DataFrame(np.arange(16).reshape(4,-1),index=['a','r','e','d'],columns=['N1','N2','N3','N4'])
se = Series(np.arange(4),index=['N1','N2','N3','N4'])

#append(),添加行
print(frame1)
print(frame2)
print(frame1.append(frame2,sort=False))
#添加series的name属性，在新的DataFrame中作为行索引名称
# se.name ='d'
# print(frame1.append(se))
#ignore_index,忽略索引，自动更新行列索引值
print(frame1.append(se,ignore_index=True))

#concat()即可以添加行，还可以添加列
#keys.设置关键字，形成多重 索引
print(pd.concat([frame1,frame2],sort=False,keys=['frame1','frame2']))
print(pd.concat([frame2,frame3],axis=1))
#join,控制拼接方式，‘inner'，行/列取交集，'outer'，行列取并集
print(pd.concat([frame2,frame3],axis=1,join='inner',ignore_index=True))




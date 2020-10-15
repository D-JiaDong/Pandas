#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
#多重索引
index= [['a','a','a','a','b','b','c','d'],['N1','N2','N3','N4','N2','N4','N3','N2']]
se = Series(np.arange(8),index=index)
print(se)

mul_arrays = pd.MultiIndex.from_arrays([['a','a','a','a','b','b','c','d'],['N1','N2','N3','N4','N2','N4','N3','N2']])
print(type(mul_arrays))
se = Series(np.arange(8),index=mul_arrays)
print(se)
mul_tuples = pd.MultiIndex.from_tuples([('a','N1'),('a','N2'),('b','N1'),('c','N2')])
se = Series(np.arange(4),index=mul_tuples)
print(se)
#笛卡尔积,优点：快捷，方便；缺点：外层的每个索引对应的内层索引都要保持一致。
#[a,b] [c,d]=[a,c],[a,d],[b,c],[b,d]
mul_product=pd.MultiIndex.from_product([['a','b'],['c','d']],names=['outter','inner'])
se = Series(np.arange(4),index=mul_product)
print(se)
print(se.index)
print(se.index[1])

#如何筛选的
frame=DataFrame(np.arange(16).reshape(4,4),\
                index=[['上半年','上半年','下半年','下半年'],['第一季度','第二季度','第一季度','第二季度']],\
                columns = [['蔬菜','蔬菜','水果','水果'],['茄子','土豆','橘子','苹果']])
print(frame)
print(frame.蔬菜.土豆)
print(frame['蔬菜','土豆'])
#对行和列同时进行索引 使用.loc[(行),(列)]
print(frame.loc[('上半年','第一季度'),('水果','橘子')])
print(frame.iloc[0])
print(frame.iloc[[0,1]])
print(frame.iloc[[0,1],1:])

#pandas 读取.csv,Excel,数据库，json文件，
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
data=pd.read_csv('D:\python视频\\breast-cancer-wisconsin (1).csv')
#print(data.head(100))
data=pd.read_csv("D:\python视频\\breast-cancer-wisconsin (1).csv")
#print(data)
print((data['Bare Nuclei']=='?').sum())
data=data.replace(to_replace='?',value=np.nan)
print((data['Bare Nuclei']=='?').sum())
print((data['Bare Nuclei']).count())
data=data.dropna(how='any')
#print(data.shape)
# data.to_csv(r'D:\python视频\breast-cancer-wisconsin (3).csv',index=0)


#json，网络传输数据的文件格式，类似于字典
import json
with open('D:\python视频\products.json','r',encoding='utf8')as fp:
    data=json.load(fp)
print(data)
df=DataFrame(data)
print(df)

#excel
# data=pd.ExcelFile('D:\python视频\excel_read.xls')
# print(data)
# print(data.parse('list_3'))
# print(data.parse('list',header=None))
#
# df=pd.DataFrame([[1,2,3],[4,5,6]])
# wri=pd.ExcelFile(r'D:\python视频\excel_read.xls')
# df.to_excel(wri,sheet_name='df_new')
# wri.save()


#pandas 可视化
import matplotlib.pyplot as plt
s=pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
print(s)
s.plot(color='pink',marker='*',style='--',xticks=range(0,100,20),label='line')
plt.show()


df=pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=list('ABCD'),index=np.arange(0,100,10))
print(df)
df.plot()
plt.show()
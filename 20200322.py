#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
import json
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
#对行和列同时进行筛选，使用.loc[(行),（列）]
print(frame.loc[('上半年','第一季度'),('水果','橘子')])
#使用下标进行筛选，下标是内层索引的下标
print(frame.iloc[0])
print(frame.iloc[[0,1]])
print(frame.iloc[[0,1],1:])

# #pandas 读取.csv,数据库，json文件，Excel
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# #skiprows=n,跳过几行再读取,header=None，没有列名称，DataFrame自动赋值列名称，nrows=取哪些行,dtype=?,设置数据是什么类型
# data = pd.read_csv(r'D:\1-zr\晚班-02\20200322\breast-cancer-wisconsin (1).csv')
# print(data.head(15))
# # data = pd.read_csv(r'D:\1-zr\晚班-02\20200322\breast-cancer-wisconsin (1).csv',nrows=10)
# # print(data.dtypes)
# print('-------------------------------------------------')
# print((data['Bare Nuclei']=='?').sum())
# data = data.replace(to_replace = '?',value=np.nan)
# print((data['Bare Nuclei']=='?').sum())
# print(data['Bare Nuclei'].count())
# data = data.dropna(how ='any')
# print(data.shape)
# #index = 0不将行索引进行存储，header=None/0，不保存列索引
# data.to_csv(r'D:\1-zr\晚班-02\20200322\breast-cancer-wisconsin (2).csv',index=0,header=None)


#！！！！！！！！！对数据库进行读取数据
#json,网络传输数据的文件格式，类似于字典
#'r'只读文件，'w'写，'rw'又读又写
#

with open(r'D:\1-zr\晚班-02\20200322\products.json','r',encoding='utf8') as fp:
    data = json.load(fp)

print(data)
print(type(data))
df = DataFrame(data)
print(df)


#读写excel文件,ExcelFile()
data = pd.ExcelFile(r'D:\1-zr\晚班-02\20200322\excel_read.xls')
print(data)
#parse（）选择sheet页函数
print(data.parse('list_3'))
print(data.parse('list',header=None))

df = pd.DataFrame([[1,2,3],[4,5,6]])
writer = pd.ExcelWriter(r'D:\1-zr\晚班-02\20200322\df.xls')
df.to_excel(writer,sheet_name='df_new')
writer.save()


#pandas 可视化
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(221)
#Series绘画，行索引对应X轴值，数据对应y轴值
s = pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
print(s)
#kind=line，bar,pie,选择不同图形绘制
s.plot(color='pink',marker='*',style='--',xticks=range(0,100,20),label='line',\
                title='plot',legend=True,fontsize=10,ax=ax1)#,ylim=(-2,2)
# plt.show()
ax2 = fig.add_subplot(222)
se = Series([10,25,30,13,22],index=list('abcde'))
se.plot(kind='pie',explode=[0,0,0,0,0.1],radius=1.3,labeldistance=0.5,shadow=True)
plt.show()

#使用DataFrame画图，行索引对应x轴值，列索引，对应的就是多个对象（个体），数据对应y轴值
df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=list('ABCD'),index=np.arange(0,100,10))
print(df)
df.plot(style='--',marker='*')
plt.show()

df.plot(kind='barh',stacked=True)
plt.show()


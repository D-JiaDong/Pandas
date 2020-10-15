import pandas as pd
import numpy as np
from pandas import Series
from pandas import  DataFrame

s1=Series([1,2,3],index=list('abc'))
#删除操作
print(s1.drop('a'))
print(s1)
#inplace 默认为false,生成视图不在原Series上进行操作
#若想改变原Series,可将inplace=True
s1.drop('a',inplace=True)
print(s1)
#删除多行s1.drop(['b','c'])



df=DataFrame({'a':[1,1,1],'b':[2,2,2],'c':[3,3,3]})
#axis默认0,对行的方向列进行处理，axis=1,对列的方向进行行处理

#使用下标进行删除
print(df.drop(df.index[1]))
print(df.drop(df.columns[1],axis=1))

df=DataFrame({'a':[1,1,1],'b':[2,2,2],'c':[3,3,3]})
print(df)
print(df.dropna(how='any'))
print(df.dropna(how='all',axis=1))

print(df.dropna(thresh=2,axis=1))

#排序
df=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('abc'),index=['one','two','three','four'])
#默认升序 由小到大
print(df)
#根据索引排序
print(df.sort_index())
print(df.sort_index(ascending=False))
print(df.sort_index(ascending=False,axis=1))
#根据数值排序
print(df.sort_values(by=['a','b'],ascending=False))
#replace()替换，
print(df.replace(to_replace=5,value=555))


#DataFrame属性
print(df.values)
print(df.index)#行索引
print(df.columns)
df.index.name='NO'
df.columns.name='NN'

#head()返回前几行值
df.head(n=1)
#返回后几行
df.tail(n=2)

#数据统计函数
se=Series([2,2,3,4,1])
#去重
print(se.unique())
#计算Series的频数
print(se.value_counts())
#数据统计函数
#count 非空数值有几个，mean平均值
print(se.describe())

df=DataFrame(np.arange(12).reshape(3,4),columns=list('abcd'))
arr=np.arange(12).reshape(3,4)
print(arr.transpose())
print(arr)


#多个DataFrame进行运算

#优点数据对齐
df1=DataFrame(np.arange(12).reshape(3,4),columns=list('abcd'))
df2=DataFrame(np.arange(20).reshape(4,5),columns=list('abcde'))
print(df1)
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=0))
print(df1.mul(df2,fill_value=1))
#广播
se=df1.loc[0]
print(df1)
print(se)
print(df1-se)


#DataFrame 合并
frame1=DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'],columns=['N1','N2','N3','N4'])
frame2=DataFrame(np.arange(16).reshape(4,-1),index=['a','b','c','d'],columns=['N1','N2','N3','N4'])
frame3=DataFrame(np.arange(16).reshape(4,-1),index=['a','r','e','d'],columns=['N1','N2','N3','N4'])
se=Series(np.arange(4),index=['N1','N2','N3','N4'])
se.name='d'
#appand(),添加行，不可以添加列
print(frame1)
print(frame2)
print(frame1.append(frame2,sort=False))
print(frame1.append(se))
#忽略行索引
print(frame1.append(se,ignore_index=True))

print(pd.concat([frame1,frame2],sort=False,keys=['frame1','frame2']))
#从行上增加
print(pd.concat([frame2,frame3],axis=1))
#join控制拼接方式
print(pd.concat([frame2,frame3],axis=1))

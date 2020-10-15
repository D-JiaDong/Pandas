#!/usr/bin/env python
# -*- coding:utf-8 -*-

#将Series和DataFrame对象转换成其他对象，list，dict，datatime
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(10).reshape(5,2),columns=list('ab'))
print(df)
se = df['a']
print(type(se))
#将Series和DataFrame转换成list对象
print(se.tolist())
print(df.values.tolist())
se[3]=4
print(se)
#drop_duplicates()删除重复值
print(se.drop_duplicates().tolist())
print(type(se.drop_duplicates().tolist()))

#转换成字典,to_dict(),orient='record'
print(df.to_dict())
print('-------------------------------------------------')
#orient='record',每一行都是一个字典,整体是一个list
print(df.to_dict(orient='records'))
#orient='list',每一列都是一个列表，列名称对应字典中的键值
print(df.to_dict(orient='list'))
#orient='series',列名称对应键值，值，series对象
print(df.to_dict(orient='series'))
#orient='split',键值是index，columns，data
print(df.to_dict(orient='split'))
print(df.to_dict(orient='dict'))

#pandas转换中数据转换成时间格式，datatime对象,年月日（必填）时分秒
#可以将字符串转换成时间形式
print(pd.to_datetime('2018/12/20 19:59:13'))
print(type(pd.to_datetime('2018/12/20')))
time1 =pd.to_datetime('2020/03/27 12:34:23')
time2 = pd.to_datetime('2018/03/27 14:12:11')
print(time1-time2)
#时间差对象
print(type(time1-time2))




import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(10).reshape(5,2),columns=list('ab'))

print(df)
se=df['a']
print(type(se))
print(se.tolist())
print(df.values.tolist())
se[3]=4
print(se)
#删除 去重
print(se.drop_duplicates())
#print(se.drop_duplicates().tolist())

#转换字典 .to_dict(),不要行索引orient='record'整体list
print(df.to_dict(orient='dict'))#默认形式 可不写参数
#不要行索引orient='record'整体list,每一行都是一个字典
print(df.to_dict(orient='record'))
#不要行索引orient='list'每一列都是一个列表 列名对应字典中的键值
print(df.to_dict(orient='list'))
#不要行索引orient='serise'列名对应键值  serise 对象
print(df.to_dict(orient='serise'))
#不要行索引orient='split'键值是index columns data
print(df.to_dict(orient='split'))


#pandas转换datatime格式，datatime对象,年月日(必填)   时分秒
print(type(pd.to_datetime('2018/12/20')))
time1=pd.to_datetime('2018/12/20 12:34:23')
time2=pd.to_datetime('2020/03/27 14:12:11')
print(time1-time2)
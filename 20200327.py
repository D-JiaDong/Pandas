#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    作业：
    NGSIM 美国联邦公路管理局，每隔十分之一秒，取前5000条设置
    1.当前车辆的动作是什么'movement'，1.直行，2左转，3右转,land_id(1,2,3,4,5)
    2.添加前车速度和加速度两列，preceding=0,前面没车，速度加速度都设置为0
    3.找到后车，再添加后车速度和加速度两列，没后车，速度加速度都设置为0
'''
import pandas as pd
#1.当前车辆的动作是什么'movement'，1.直行，2左转，3右转,land_id(1,2,3,4,5)
#data = pd.read_csv(r'D:\1-zr\晚班-02\20200322\trajectories-0750am-0805am_steer.csv')
data = pd.read_csv(r'D:\1-zr\晚班-02\20200322\trajectories-0750am-0805am_steer_02.csv',index=0)
print(data.head())
print(data.shape)
vehicle_id = data['Vehicle_ID']
lane_id = data['Lane_ID']
# for i in range(4999):# range(len(data)-1)
#     print('循环次数:%d'%i)
#     if vehicle_id[i] ==vehicle_id[i+1]:
#         if lane_id[i]==lane_id[i+1]:
#             data.loc[i,'Movement']=1
#         elif lane_id[i]>lane_id[i+1]:
#             data.loc[i,'Movement']=2
#         else:
#             data.loc[i,'Movement']=3
#     else:
#         data.loc[i,'Movement'] = 1
# data.to_csv(r'D:\1-zr\晚班-02\20200322\trajectories-0750am-0805am_steer_02.csv')
#添加前车速度和加速度两列，preceding=0,前面没车，速度加速度都设置为0
for i in range(4999):
    print(i)
    pre_id = data.loc[i,'Preceding']
    frame_id = data.loc[i,'Frame_ID']
    if pre_id!=0:
        #找到本行数据，前车的那一行数据
        #布尔索引
        data_temp =data[(data['Vehicle_ID']==pre_id)&(data['Frame_ID']==frame_id)]
        #print(type(data_temp['v_Vel']))
        if len(data_temp)!=0:
            data.loc[i,'Pre_v_Vel'] = data_temp.loc[data_temp.index[0],'v_Vel']
            data.loc[i,'Pre_v_Acc'] = data_temp.loc[data_temp.index[0],'v_Acc']
        #3.找到后车，再添加后车速度和加速度两列
        #没给后车id，但是给了前车id，那么本车（当前行数据）就是前车的后车
        #相当于，给前车添加后车id，而不是给本车添加后车id
        data.loc[data_temp.index[0],'Back_v_Vel'] = data.loc[i,'v_Vel']
        data.loc[data_temp.index[0],'Back_v_Acc'] = data.loc[i,'v_Acc']
data.to_csv(r'D:\1-zr\晚班-02\20200327\trajectories-0750am-0805am_steer_03.csv',index = 0)

#1.周围车（左前，左后，右前，右后）的速度和加速度,车辆编号，条件:纵向距离差<90,如果没有车的话就赋值为0

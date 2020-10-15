#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1.周围车（左前，左后，右前，右后）的速度和加速度,l，
  条件:纵向距离差<90,如果没有车的话就赋值为0
'''

import pandas as pd
import numpy as np
data = pd.read_csv(r'D:\1-zr\晚班-02\20200322\trajectories-0750am-0805am_steer.csv')
print(data.head())
#寻找左后车，1.时刻相同，Frame_ID   2.左后车，车道=本车车道-1
#            3.本车的Local_Y>左后车的Local_Y，4.纵向距离差<90
#寻找左前车1.时刻相同，Frame_ID   2.左前车，车道=本车车道-1
#          3.本车的Local_Y<左前车的Local_Y，4.纵向距离差<90
#寻找右后车，1.时刻相同，Frame_ID   2.左后车，车道=本车车道+1
#            3.本车的Local_Y>右后车的Local_Y，4.纵向距离差<90
#寻找右前车1.时刻相同，Frame_ID   2.右前车，车道=本车车道+1
#          3.本车的Local_Y<右前车的Local_Y，4.纵向距离差<90

for i in range(5000):
    print('循环次数：',i)
    car = data.loc[i]
    #1.时刻相同，Frame_ID   2.左后车，车道=本车车道-1
    F_left = data[(data['Frame_ID']==car['Frame_ID'])&(data['Lane_ID']==car['Lane_ID']-1)]
    #3.找到全部左后车，本车的Local_Y>左后车的Local_Y
    F_left_back = F_left[F_left['Local_Y']<car['Local_Y']]
    if len(F_left_back)!=0:  #有左后车
        print(car[['Vehicle_ID','Frame_ID']])
        print(F_left_back)
        #idxmax(),返回最大元素行索引
        left_back_index = F_left_back['Local_Y'].idxmax()
    #     #4.纵向距离差<90
        if car['Local_Y']-data.loc[left_back_index,'Local_Y']<=90:
            print('------------------------------------------------')
            data.loc[i,'left_back_v_vel'] = data.loc[left_back_index,'v_Vel']
            data.loc[i, 'left_back_v_acc'] = data.loc[left_back_index, 'v_Acc']
            data.loc[i, 'left_back_vehicle_id'] = data.loc[left_back_index, 'Vehicle_ID']
        else:#没有左后车
            data.loc[i, 'left_back_v_vel'] = 0
            data.loc[i, 'left_back_v_acc'] = 0
            data.loc[i, 'left_back_vehicle_id'] = 0
    else: #没有左后车
        data.loc[i,'left_back_v_vel'] = 0
        data.loc[i, 'left_back_v_acc'] = 0
        data.loc[i, 'left_back_vehicle_id'] = 0






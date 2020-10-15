# import numpy as np
# import pandas as pd
# from pandas import Series
# from pandas import DataFrame
#
#
# data=pd.read_csv(r'D:\python视频\trajectories-0750am-0805am_steer.csv',nrows=6000)
# frame=DataFrame(data)
# index=frame.index
# movement=[]
# frame_add=DataFrame(np.zeros((5000,4)).astype(np.float),index=np.arange(5000),columns=[ 'front_v_Vel','front_v_Acc',\
#                                                                                  'behind_v_Vel','behind_v_Acc'])
#
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)
# #转换为numpy数组
# #获取车辆当前车道位置
# lane_id=frame.loc[:,'Lane_ID']
# lane_id=np.array(list(lane_id))
# #获取帧标识号
# frame_id=frame.loc[:,'Frame_ID']
# frame_id=np.array(list(frame_id))
# #获取车辆识别号
# vehicle_id=frame.loc[:,'Vehicle_ID']
# vehicle_id=np.array(list(vehicle_id))
#
# #遍历赋值
# for i in range(5000):
#     #第一问 移动状态
#      if lane_id[i]==lane_id[i+1]:
#        movement.append('TH')
#      elif lane_id[i]>lane_id[i+1]:
#          movement.append('LT')
#      else:
#          movement.append('RT')
#     #第二问：前后车速度和及速度
#      if frame.loc[i,'Preceding']!=0:
#          #如果前方有车 获取前方车辆id 和当前帧数
#          front_id=frame.loc[i,'Preceding']
#          local_time=frame.loc[i,'Frame_ID']
#          bo1 = (vehicle_id == front_id)
#          bo2 = (frame_id == local_time)
#          print(bo1.sum())
#          print(bo2.sum())
#          arr = np.where(bo2 & bo1, frame.loc[i,'v_Vel'], 0)
#          frame_add.loc[i,'front_v_Vel']=arr.sum()
#          arr = np.where(bo2 & bo1, frame.loc[i,'v_Acc'], 0)
#          frame_add.loc[i, 'front_v_Acc'] = arr.sum()
#      else:
#          pass
#     # 如果后方有车 获取后方车辆id 和当前帧数
#      behind_id = frame.loc[i, 'Vehicle_ID']
#      local_time = frame.loc[i, 'Frame_ID']
#      bo1 = (vehicle_id == behind_id)
#      bo2 = (frame_id == local_time)
#      arr = np.where(bo2 & bo1, frame.loc[i,'v_Vel'], 0)
#      frame_add.loc[i, 'behind_v_Vel'] = arr.sum()
#      arr = np.where(bo2 & bo1, frame.loc[i,'v_Acc'], 0)
#      frame_add.loc[i, 'behind_v_Acc'] = arr.sum()
#
# #合并写入新文件
# frame_add.insert(0,'movement',np.array(movement))
# df=pd.concat([frame,frame_add],axis=1)
# df.to_csv(r'D:\python视频\add.csv')
# print(df)
#
#
#


import pandas as pd
data=pd.read_csv(r'D:\python视频\trajectories-0750am-0805am_steer.csv')
#print(data.head)
#print(data.shape)
vehicle_id=data['Vehicle_ID']
lane_id=data['Lane_ID']
# for i in range(4999):
#     if vehicle_id[i]==vehicle_id[i+1]:
#         if lane_id[i]==lane_id[i+1]:
#             data.loc[i,'Movement']=1
#         elif lane_id[i]>lane_id[i+1]:
#             data.loc[i,'Movement']=2
#         else:
#             data.loc[i,'Movement']=3
#     else:
#         data.loc[i, 'Movement'] = 1
# data.to_csv(r'D:\python视频\movement.csv')

for i in range(5000):
    pre_id=data.loc[i,'Preceding']
    frame_id=data.loc[i,'Frame_ID']
    if pre_id!=0:
        #布尔索引
        data_temp=data[(data['Vehicle_ID']==pre_id)&(data['Frame_ID']==frame_id)]
        if len(data_temp)!=0:
            data.loc[i,'Pre_v_Vel']=data_temp.loc[data_temp.index[0],'v_Vel']
            data.loc[i,'Pre_V_Acc']=data_temp.loc[data_temp.index[0],'v_Acc']
            data.loc[data_temp.index[0],'Back_v_Vel']=data.loc[i,'v_Vel']
            data.loc[data_temp.index[0], 'Back_v_Acc'] = data.loc[i,'v_Acc']
data.to_csv(r'D:\python视频\ac.csv')
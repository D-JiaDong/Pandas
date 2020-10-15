import pandas as pd
data = pd.read_csv(r'D:\python学习\车辆数据处理\trajectories-0750am-0805am_steer.csv')
print(data.head())
##'Vehicle_ID', 'Frame_ID', 'Local_X', 'Local_Y', 'v_length', 'v_Width',
# 'v_Class', 'v_Vel', 'v_Acc', 'Lane_ID', 'Preceding', 'Space_Headway'],
# dtype='object'

for i in range(999):
   print(i)
   data.loc[i, 'L_F_Vel'] = 0
   data.loc[i, 'L_F_Acc'] = 0
   data.loc[i, 'R_F_Vel'] = 0
   data.loc[i, 'R_F_Acc'] = 0
   frame_id = data.loc[i, 'Frame_ID']
   lane_id = data.loc[i, 'Lane_ID']
   local_y = data.loc[i, 'Local_Y']
   bo=(\
        data['Frame_ID'] == frame_id \
        &\
        ((data['Lane_ID'] == lane_id - 1) | (data['Lane_ID'] == lane_id + 1))\
        &\
        ((local_y-data['Local_Y'])*(local_y-data['Local_Y'])<=90*90)
      )
   #print(bo.sum())
   data_i_s=data[bo]
   if 1-data_i_s.empty:
        print('***********************************************')
        for data_i in data_i_s:
            if data_i['Lane_ID'] == lane_id - 1 & local_y - data_i['Local_Y'] <= 0 & data.loc[i, 'L_F_Vel'] != 0:
                 data.loc[i, 'L_F_Vel'] = data['v_Vel']
                 data.loc[i, 'L_F_Acc'] = data['v_Acc']
            elif data_i['Lane_ID'] == lane_id - 1 & local_y - data_i['Local_Y'] > 0 & data.loc[i, 'L_B_Vel'] != 0:
                 data.loc[i, 'L_B_Vel'] = data['v_Vel']
                 data.loc[i, 'L_B_Acc'] = data['v_Acc']
            elif data_i['Lane_ID'] == lane_id + 1 & local_y - data_i['Local_Y'] <= 0 & data.loc[i, 'R_F_Vel'] != 0:
                 data.loc[i, 'R_F_Vel'] = data['v_Vel']
                 data.loc[i, 'R_F_Acc'] = data['v_Acc']
            else:
                data.loc[i, 'R_B_Vel'] = data['v_Vel']
                data.loc[i, 'R_B_Acc'] = data['v_Acc']
            if(data.loc[i, 'L_F_Vel'] != 0 & data.loc[i, 'L_B_Vel'] != 0 & data.loc[i, 'R_F_Vel'] !=0 & data.loc[i, 'R_B_Vel'] !=0):
                break
data.to_csv(r'D:\python学习\车辆数据处理\around.csv')

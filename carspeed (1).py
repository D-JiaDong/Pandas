import pandas as pd
#1.当前车辆的动作是什么'movement'，1.直行，2左转，3右转,land_id(1,2,3,4,5)
# data = pd.read_csv(r'D:\中软国际课件\人工智能课件\trajectories-0750am-0805am_steer.csv')
# data = pd.read_csv(r'D:\中软国际课件\人工智能课件\trajectories-0750am-0805am_steer_1.csv')
data = pd.read_csv(r'D:\中软国际课件\人工智能课件\trajectories-0750am-0805am_steer_2.csv',)
print(type(data))
Vehicle_ID = data['Vehicle_ID']
# land_id = data['Lane_ID']
# for i in range(4999):
#     if Vehicle_ID[i] == Vehicle_ID[i+1]:
#         if land_id[i] ==land_id[i+1]:
#             data.loc[i,'Movement'] = 1
#         elif land_id[i] < land_id[i+1]:
#             data.loc[i,'Movement'] = 3
#         else:
#             data.loc[i, 'Movement'] = 2
#     else:
#         data.loc[i,'Movement'] = 1
# data.to_csv(r'D:\中软国际课件\人工智能课件\trajectories-0750am-0805am_steer_1.csv')
#添加前车速度和加速度两列，preceding=0,前面没车，速度加速度都设置为0
for i in range(4999):
    print(i)
    # pre_id = data.loc[i, 'Preceding']
    frame_id = data.loc[i, 'Frame_ID']
    local_y = data.loc[i, 'Local_Y']
    land_id = data.loc[i,'Lane_ID']
    # if pre_id != 0:
    #     data_temp = data[(data['Vehicle_ID'] == pre_id) & (data['Frame_ID'] == frame_id)]
    #     if len(data_temp) != 0:
    #         data.loc[i, 'Pre_v_Vel'] = data_temp.loc[data_temp.index[0], 'v_Vel']
    #         data.loc[i, 'Pre_v_Acc'] = data_temp.loc[data_temp.index[0], 'v_Acc']
    #          #3.找到后车，再添加后车速度和加速度两列
    #     data.loc[data_temp.index[0], 'Back_v_Vel'] = data.loc[i, 'v_Vel']
    #     data.loc[data_temp.index[0], 'Back_v_Acc'] = data.loc[i, 'v_Acc']
    data_around = data[(data['Frame_ID'] == frame_id) & (abs(data['Local_Y']-local_y) < 90)]
    # print(data_around.shape)
    if len(data_around) != 0:
        for j in range(data_around.shape[0]):
            # print(j)
            # print(type(local_y))
            # print(data_around.loc[data_around.index[j],'Local_Y'])
            # print(type(data_around.loc[data_around.index[j],'Local_Y']))
            if (data_around.loc[data_around.index[j], 'Local_Y'] - local_y) > 0:
                if data_around.loc[data_around.index[j], 'Lane_ID'] < land_id:
                    data.loc[i, 'Ar_lu_ID'] = data_around.loc[data_around.index[j], 'Vehicle_ID']
                    data.loc[i, 'Ar_lu_v_Vel'] = data_around.loc[data_around.index[j], 'v_Vel']
                    data.loc[i, 'Ar_lu_v_Acc'] = data_around.loc[data_around.index[j], 'v_Acc']
                elif data_around.loc[data_around.index[j], 'Lane_ID'] > land_id:
                    data.loc[i, 'Ar_ru_ID'] = data_around.loc[data_around.index[j], 'Vehicle_ID']
                    data.loc[i, 'Ar_ru_v_Vel'] = data_around.loc[data_around.index[j], 'v_Vel']
                    data.loc[i, 'Ar_ru_v_Acc'] = data_around.loc[data_around.index[j], 'v_Acc']
            elif (data_around.loc[data_around.index[j], 'Local_Y'] - local_y) < 0:
                if data_around.loc[data_around.index[j], 'Lane_ID'] < land_id:
                    data.loc[i, 'Ar_ld_ID'] = data_around.loc[data_around.index[j], 'Vehicle_ID']
                    data.loc[i, 'Ar_ld_v_Vel'] = data_around.loc[data_around.index[j], 'v_Vel']
                    data.loc[i, 'Ar_ld_v_Acc'] = data_around.loc[data_around.index[j], 'v_Acc']
                elif data_around.loc[data_around.index[j], 'Lane_ID'] > land_id:
                    data.loc[i, 'Ar_rd_ID'] = data_around.loc[data_around.index[j], 'Vehicle_ID']
                    data.loc[i, 'Ar_rd_v_Vel'] = data_around.loc[data_around.index[j], 'v_Vel']
                    data.loc[i, 'Ar_rd_v_Acc'] = data_around.loc[data_around.index[j], 'v_Acc']
    # else:
    #     data.loc[i,['Ar_lu_ID','Ar_lu_v_Vel','Ar_lu_v_Acc','Ar_ru_ID','Ar_ru_v_Vel','Ar_ru_v_Acc','Ar_ld_ID',
    #                 'Ar_ld_v_Vel','Ar_ld_v_Acc','Ar_rd_ID','Ar_rd_v_Vel','Ar_rd_v_Acc']] = 0
data.to_csv(r'D:\中软国际课件\人工智能课件\trajectories-0750am-0805am_steer_3.csv', index=0)

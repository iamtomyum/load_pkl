import joblib
import numpy as np
import math
#肢体编号
def get_spin_joint_names():
    return [
        'OP Nose',        # 0
        'OP Neck',        # 1
        'OP RShoulder',   # 2
        'OP RElbow',      # 3
        'OP RWrist',      # 4
        'OP LShoulder',   # 5
        'OP LElbow',      # 6
        'OP LWrist',      # 7
        'OP MidHip',      # 8
        'OP RHip',        # 9
        'OP RKnee',       # 10
        'OP RAnkle',      # 11
        'OP LHip',        # 12
        'OP LKnee',       # 13
        'OP LAnkle',      # 14
        'OP REye',        # 15
        'OP LEye',        # 16
        'OP REar',        # 17
        'OP LEar',        # 18
        'OP LBigToe',     # 19
        'OP LSmallToe',   # 20
        'OP LHeel',       # 21
        'OP RBigToe',     # 22
        'OP RSmallToe',   # 23
        'OP RHeel',       # 24
        'rankle',         # 25
        'rknee',          # 26
        'rhip',           # 27
        'lhip',           # 28
        'lknee',          # 29
        'lankle',         # 30
        'rwrist',         # 31
        'relbow',         # 32
        'rshoulder',      # 33
        'lshoulder',      # 34
        'lelbow',         # 35
        'lwrist',         # 36
        'neck',           # 37
        'headtop',        # 38
        'hip',            # 39 'Pelvis (MPII)', # 39
        'thorax',         # 40 'Thorax (MPII)', # 40
        'Spine (H36M)',   # 41
        'Jaw (H36M)',     # 42
        'Head (H36M)',    # 43
        'nose',           # 44
        'leye',           # 45 'Left Eye', # 45
        'reye',           # 46 'Right Eye', # 46
        'lear',           # 47 'Left Ear', # 47
        'rear',           # 48 'Right Ear', # 48
    ]

output =joblib.load('vibe_output_yhh.pkl')
#print(output.keys(),type(output))
#得到3d坐标的维度和numpy数组
def dimension(demand):
    for k,v in output[1].items(): 
        #查看维度
        #print(k,v.shape)
        if k==demand=='joints3d':
            return v

#x保存整个视频所需要的三维坐标
x=dimension('joints3d')

#输出所有帧数的所有坐标值
def All_Coordinate():
    file = open("1.txt", "w")
    
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
                file.write('Frame:'+str(i)+'position:'+str(j)+'coordinate:'+str(x[i][j])+'\n')
'''
    输出坐标测试
'''
#All_Coordinate()

'''
    LElbow RElbow LShoulder RShoulder LWrist RWrist
    6       3       5       2           7       4
'''


def cal_ang(point_1, point_2, point_3):
    """
    根据三点坐标计算夹角
    :param point_1: 点1坐标
    :param point_2: 点2坐标
    :param point_3: 点3坐标
    :return: 暂时返回point_2的角度
    """
    a=math.sqrt((point_2[0]-point_3[0])**2+(point_2[1]-point_3[1])**2+(point_2[2]-point_3[2])**2)
    b=math.sqrt((point_1[0]-point_3[0])**2+(point_1[1]-point_3[1])**2+(point_1[2]-point_3[2])**2)
    c=math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2+(point_1[2]-point_2[2])**2)
    A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
    B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
    C=math.degrees(math.acos((c*c-a*a-b*b)/(-2*a*b)))
    return B
 
#print(cal_ang((0, 0, 0), (1, 1, 1), (0, 1, 1)))

def getAngle():
    file = open("2.txt", "w")
    for i in range(x.shape[0]):
        #每一帧的肘关节角度
        #print("Frame:{0},L:{1},R:{2}".format(i,cal_ang(x[i][5],x[i][6],x[i][7]),cal_ang(x[i][2],x[i][3],x[i][4])))
        file.write("Frame:{0},L:{1},R:{2}".format(i,cal_ang(x[i][5],x[i][6],x[i][7]),cal_ang(x[i][2],x[i][3],x[i][4])))
    print("Work done")
getAngle()

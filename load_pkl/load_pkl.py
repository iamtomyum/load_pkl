import joblib
import numpy as np
output =joblib.load('vibe_output_fkl.pkl')
print(output.keys(),type(output))
#得到3d坐标的维度和numpy数组
def dimension(demand):
    for k,v in output[1].items(): 
        #查看维度
        #print(k,v.shape)
        if k==demand=='joints3d':
            return v
#输出所有帧数的所有坐标值
def All_Coordinate():
    file = open("1.txt", "w")
    x=dimension('joints3d')
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
                file.write('Frame:'+str(i)+'position:'+str(j)+'coordinate:'+str(x[i][j])+'\n')
#输出坐标测试
All_Coordinate()
#接下来需要匹配检查点

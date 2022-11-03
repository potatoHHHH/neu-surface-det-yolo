import pandas as pd
import os
import random
import shutil
# ma={}
lis=os.listdir(r'D:\dpl\project\datasets\NEU-DET\train_images')
# for i in lis:
#     ii=i.split('.')[0]
#     ma[ii]=1
# lis2=os.listdir(r'D:\dpl\project\datasets\NEU-DET\train_images')
# for i in lis2:
#     ii=i.split('.')[0]
#     if ma.get(ii)==None:
#         os.remove(rf'D:\dpl\project\datasets\NEU-DET\train_images\{i}')
num=len(lis)
ind_lis=[i for i in range(num)]
random.shuffle(ind_lis)
train_ind=ind_lis[:-1000]
val_ind=ind_lis[-1000:]
for ind in val_ind:
    img=lis[ind]
    shutil.move(rf'D:\dpl\project\datasets\NEU-DET\train_images\{img}',rf'D:\dpl\project\datasets\NEU-DET\validation_images\{img}')
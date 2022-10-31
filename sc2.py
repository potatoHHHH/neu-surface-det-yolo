import os
import shutil
train_label=os.listdir(r'D:/dpl/project/datasets/NEU-DET/train/labels')
val_label=os.listdir(r'D:/dpl/project/datasets/NEU-DET/train/labels')
clsm=["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]
for cls in clsm:
    if not  os.path.exists(rf'D:/dpl/project/datasets/NEU-DET/train/labels/{cls}'):
        os.makedirs(rf'D:/dpl/project/datasets/NEU-DET/train/labels/{cls}')
for label in train_label:
    cls=label.split('_')[0] if len(label.split('_'))==2 else '_'.join(label.split('_')[0:2])
    if label.find('.txt')!=-1:
        shutil.copyfile(rf'D:/dpl/project/datasets/NEU-DET/train/labels/{label}',f'D:/dpl/project/datasets/NEU-DET/train/labels/{cls}/{label}')
    

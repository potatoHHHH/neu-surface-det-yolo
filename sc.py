import os
import shutil
train_label=os.listdir(r'D:\dpl\project\datasets\NEU-DET\train\labels')
val_label=os.listdir(r'D:\dpl\project\datasets\NEU-DET\validation\labels')
clsm=["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]
# for cls in clsm:
    # os.makedirs(rf'D:\dpl\project\datasets\NEU-DET\train\labels\{cls}')
for label in train_label:
    cls=label.split('_')[0] if len(label.split('_'))==2 else '_'.join(label.split('_')[0:2])
    print(cls)
    # shutil.copyfile(f'D:\dpl\project\datasets\NEU-DET\train\labels\{label}',f'D:\dpl\project\datasets\NEU-DET\train\labels\{cls}\{label}')
    
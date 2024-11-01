import torch
import torchvision.transforms as T

class Config(object):
# training dataset
    data_list = f"/kaggle/input/data_list/pytorch/default/1/data_list.txt"
    clip_model = '/kaggle/input/clib-fiqa/pytorch/default/1/RN50.pt'
# save settings
    checkpoints = f"/kaggle/working/checkpoints"   
# training settings
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    seed = 323
    pin_memory = True
    num_workers = 12
    batch_size = 32         
    epoch = 25
    lr = 5e-6
    weight_decay = 0.001
    Epo_th = 5
    saveModel_epoch = 5

config = Config()

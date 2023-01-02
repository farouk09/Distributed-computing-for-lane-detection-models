import os
import argparse
import time
import csv
import PIL
import random
import numpy as np
import torch, torchvision
from torchvision import transforms
from torchvision import models
import torch.backends.cudnn as cudnn
from PIL import Image


def get_image(filename, input_size):
  im = Image.open(filename)
  im_process = transforms.Compose([transforms.Resize([input_size, input_size]),transforms.ToTensor()])
  im = im_process(im)
  return im.unsqueeze(0)

def set_seed(seed):
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)


if __name__ == "__main__" :

    set_seed(0)
    device = torch.device(0)
    stream_ = torch.cuda.Stream(device=device)

    images = []
    times = []

    net = models.vgg16(pretrained=False)
    net.cuda()
    net.eval()

    starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)

    repetitions = 50
    timings=np.zeros((repetitions,1))

    x = torch.randn(1, 3, 224, 224).cuda()

    with torch.cuda.stream(stream_):
        #GPU-WARM-UP
        for _ in range(100):
            _ = net(x)

        # MEASURE PERFORMANCE
        with torch.no_grad():
            for rep in range(repetitions):
                starter.record()
                _ = net(x)
                # WAIT FOR GPU SYNC
                ender.record()
                torch.cuda.synchronize()
                curr_time = starter.elapsed_time(ender)
                timings[rep] = curr_time

        mean_syn = np.sum(timings)
        std_syn = np.std(timings)

        print(mean_syn/repetitions)
        

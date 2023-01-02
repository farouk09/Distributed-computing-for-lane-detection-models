# Distributed-computing-for-lane-detection-models
Distributed inference between edge devices for lane detection models.

## **Framework used**

*PytorchAutoDrive* is a **pure Python** framework includes semantic segmentation models, lane detection models based on **PyTorch**. Here we provide full stack supports from research (model training, testing, fair benchmarking by simply writing configs) to application (visualization, model deployment).

**Paper:** [Rethinking Efficient Lane Detection via Curve Modeling](https://arxiv.org/abs/2203.02431) (CVPR 2022)

**Poster:** [PytorchAutoDrive: Toolkit & Fair Benchmark for Autonomous Driving Research](https://drive.google.com/file/d/14EgcwPnKvAZJ1aWqBv6W9Msm666Wqi5a/view?usp=sharing) (PyTorch Developer Day 2021)

*This repository is under active development, results with models uploaded are stable. For legacy code users, please check [deprecations](https://github.com/voldemortX/pytorch-auto-drive/issues/14) for changes.*

**A demo video from ERFNet:**

https://user-images.githubusercontent.com/32259501/148680744-a18793cd-f437-461f-8c3a-b909c9931709.mp4

## Highlights

Various methods on a wide range of backbones, **config** based implementations, **modulated** and **easily understood** codes, image/keypoint loading, transformations and **visualizations**, **mixed precision training**, tensorboard logging and **deployment support** with ONNX and TensorRT.

Models from this repo are faster to train (**single card trainable**) and often have better performance than other implementations, see [wiki](https://github.com/voldemortX/pytorch-auto-drive/wiki/Notes) for reasons and technical specification of models.

## Supported datasets: 

| Task | Dataset |
| :---: | :---: |
| semantic segmentation | PASCAL VOC 2012 |
| semantic segmentation | Cityscapes |
| semantic segmentation | GTAV* |
| semantic segmentation | SYNTHIA* |
| lane detection | CULane |
| lane detection | TuSimple |
| lane detection | LLAMAS |
| lane detection | BDD100K (*In progress*) |

\* The UDA baseline setup, with Cityscapes *val* set as validation.

## Supported models:

| Task | Backbone | Model/Method |
| :---: | :---: | :---: |
| semantic segmentation | ResNet-101 | [FCN](/configs/semantic_segmentation/fcn) |
| semantic segmentation | ResNet-101 | [DeeplabV2](https://arxiv.org/abs/1606.00915) |
| semantic segmentation | ResNet-101 | [DeeplabV3](https://arxiv.org/abs/1706.05587) |
| semantic segmentation | - | [ENet](https://arxiv.org/abs/1606.02147) |
| semantic segmentation | - | [ERFNet](/configs/semantic_segmentation/erfnet) |
| lane detection | ENet, ERFNet, VGG16, ResNets (18, 34, 50, 101), MobileNets (V2, V3-Large), RepVGGs (A0, A1, B0, B1g2, B2), Swin (Tiny) | [Baseline](/configs/lane_detection/baseline) |
| lane detection | ERFNet, VGG16, ResNets (18, 34, 50, 101), RepVGGs (A1) | [SCNN](https://arxiv.org/abs/1712.06080) |
| lane detection | ResNets (18, 34, 50, 101), MobileNets (V2, V3-Large) | [RESA](https://arxiv.org/abs/2008.13719) |
| lane detection | ERFNet, ENet | [SAD](https://arxiv.org/abs/1908.00821) ([*Postponed*](https://github.com/voldemortX/pytorch-auto-drive/wiki/Notes)) |
| lane detection | ERFNet | [PRNet](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123630698.pdf) (*In progress*) |
| lane detection | ResNets (18, 34, 50, 101), ResNet18-reduced | [LSTR](https://arxiv.org/abs/2011.04233) |
| lane detection | ResNets (18, 34) | [BézierLaneNet](/configs/lane_detection/bezierlanenet) |

## **Testing models on Jetson TX2 and Jetson AGX Xavier**

![image](https://user-images.githubusercontent.com/38142069/210281166-e7dab7c9-9ac3-47b6-99cc-3ef7ff725bd1.png)

## **collaborative inference method applied on road markings detection models**

Our design explores the trade-off between latency and power consumption, while taking into account different user requirements on latency and dynamic network environments. End-to-end latency includes task execution, data transmission, and serialization (the process of converting data to be transmitted to a byte stream).
We now formally formulate the task sharing problem. Let us define 𝑖 ∈ {0, 1, ... , 𝑛 + 1}, where 𝑖 is the partition point 𝑖𝑡ℎ in our model and 𝑛 is the number of layers in an N-layer deep neural network (DNN). The corresponding partition point corresponding to it is shown in the Figure below

![image](https://user-images.githubusercontent.com/38142069/210279606-e3a79d7f-5515-4166-95d6-01cf4e22614f.png)

for each DNN model and for each hardware configuration (CPU and GPU clock frequency number of cores, number of Iot! devices, etc.) we calculate the execution time and and the transmission time of each layer of the DNN in order to find the best partitioning point partitioning point that satisfies the energy consumption criteria.

![image](https://user-images.githubusercontent.com/38142069/210279218-54793414-3d92-4bef-a101-01621e4e96ea.png)

For the CNN inference, we used two embedded computing devices with GPUs that Nvidia recently started selling. In terms of computational and storage capabilities as well as GPU micro-architecture, these two platforms are completely different. 
These differences allowed us to test the portability of our approach. We give in the table below, the main characteristics of these two platforms : 

![image](https://user-images.githubusercontent.com/38142069/210279982-54a1bcd2-acb6-44f2-8262-cdf8eba0c759.png)

## **Result of the collaborative inference between the Jetson TX2 and the Jetson AGX**

For each hardware configuration, we run the partitioning algorithm before the execution of the pre-trained models in order to find the optimal partitioning point, so one part will be executed on the Jetson TX2 and the other will be executed on the Jetson AGX whose goal is to optimize the model latency and the power consumption as shown on the figure below.

![image](https://user-images.githubusercontent.com/38142069/210281359-961197f1-5981-4b95-99c6-2bfa52b39797.png)

The latency of the models before and after the collaborative inference is calculated as shown in the figure below. The orange bars show the latency before the execution of the collaborative inference algorithm between the Jetson TX2 and the AGX Xavier and the blue bars show the results of the latency optimization.
In some scenarios, we were able to accelerate the latency by a factor of 5 (see SCNN modules)

![image](https://user-images.githubusercontent.com/38142069/210281471-7a9311a2-a570-4581-90be-1ea600b09903.png)



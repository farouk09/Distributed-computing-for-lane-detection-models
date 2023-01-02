#!/bin/bash

python3 config_generator.py --cpu-freq 0.652800 --gpu-freq 0.420750 --emc-freq 0.665600;

sudo rm /etc/nvpmodel.conf;

sudo cp nvpmodel.conf /etc/;

sudo nvpmodel -m 17;

sudo jetson_clocks;

sudo jetson_clocks --show ;
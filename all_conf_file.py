import csv

cpu = [0.6528, 0.8064, 0.96, 1.1136, 1.2672, 1.4208, 1.5744, 1.728, 1.8816, 2.035]
        
gpu = [0.42075, 0.52275, 0.62475, 0.72675, 0.85425, 0.93075, 1.03275, 1.122, 1.23675, 1.3005]

emc = [0.6656, 0.8, 1.0624, 1.3312, 1.6, 1.866]

conf = []

for c in cpu:
    for g in gpu:
        for e in emc:
            conf.append([c, g, e])

with open('all_conf.txt', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    for row in conf:
        writer.writerow(row)

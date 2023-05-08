import numpy as  np
import matplotlib.pyplot as plt
from math import *

data, t = [], []
with open("data2.txt", "r") as f:
    for line in f.readlines():
        d = line.split(" ")
        t.append(float(d[0])); data.append(float(d[1]))

sim_data, sim_t = [], []
with open("simu.txt", "r") as f:
    for line in f.readlines():
        d = line.split(";")
        sim_t.append(float(d[0])); sim_data.append(float(d[1]))

fig, axs = plt.subplots(1, 2)
axs[0].plot(t,data)
axs[1].plot(sim_t[2000:], [cos(a) for a in sim_data[2000:]])
plt.show()
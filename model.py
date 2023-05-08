import matplotlib.pyplot as plt
from cmath import *
import numpy as np

#plt.style.use(['science'])

j = complex(0, 1)

r0 = 68E5
M = 10E31
G = 6.67430E-11
T = np.linspace(0.001, 1, 3440)

w0 = (G*M/(4*r0**3))**1/2
w = [w0]

a = 0.01

def g(t):
    return exp(-a*t)

'''
for t in T:
    w.append(w[-1]*(g(t))**(-3/2)*exp(-3*j*w[-1]*t/2))

f = np.array(w)/2*pi
fr = np.array(f).real
i = np.argmax(fr)
fr = fr[:i]
T = T[:i]
'''

def get(T):
    r = [r0*(exp(cos(2*w0*t)-sin(2*w0*t)-1)**3/4) for t in T]
    return [0.0001*r0**2*w0/(_**2*2*pi).real for _ in r], [_.real for _ in r]

def gauss(x, x0, dx):
    return exp(-((x-x0)/dx)**2).real


f, r = get(T)
fp, rp = get(T + 1)
VF = []
F = np.linspace(0, max(f), 3440)
Tp = np.linspace(0, max(T), 3440)

with open("simu.txt", "w") as f_:
    f_.write("\n".join([f'{Tp[i]};{f[i]}' for i in range(len(f))]))

"""
for i in range(len(Tp)):
    temp = [0]
    for _f in F[1:]:
        temp.append(gauss(_f, f[i], _f*0.5))
    VF.append(temp)

VF = np.transpose(VF)


plt.figure(figsize=(6,3))
#plt.plot(T, f, "k", lw=0.8)
cmap = plt.colormaps.get_cmap('plasma')
plt.pcolormesh(Tp, F, VF, cmap=cmap, shading='gouraud')
plt.colorbar()
plt.xlabel("Temps($10^{-2}s$)")
plt.ylabel("Fréquence (Hz)")
plt.xlim([0,max(Tp)])
plt.savefig("model_classique.png", dpi=300)
"""

mod = []
ma = np.argmax(f)
passed = False
j = 0
b = 10
for i in range(ma):
    mod.append(f[i])

for t in T[ma:]:
    mod.append(f[ma]*exp(-b*(t-T[ma])).real)

dmod = []
for i in range(len(f)-1):
    dmod.append((mod[i+1]-mod[i])/(T[i+1]-T[i]))

P = [10*log10(4*pi**2*M*mod[i]*dmod[i]) for i in range(ma)]
for i in range(ma, len(T)):
    P.append(P[ma-1]*exp(-b*(T[i]-T[ma])).real)

def get_i(L, x):
    for j in range(len(L)):
        if L[j] == x:
            return j

g = [P[get_i(T, t)]*cos(mod[get_i(T, t)]*t/(2*pi)).real for t in T]
plt.plot(T[1000:], g[1000:])
plt.show()
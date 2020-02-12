import matplotlib.pyplot as plt
import pickle

img = plt.imread('maps.png')
plt.imshow(img)
with open("coords.pickle", "rb") as fp:   # Unpickling
    a = pickle.load(fp)
for ii in range(113):
	plt.text(a[ii][0]+20, a[ii][1], ii+1, fontsize=8, bbox=dict(facecolor='red', alpha=0.5))

plt.show()

import math

d = {}
T = [ [[], [], [], []] for i in range(113+1) ]
T[0] = []
G = [[0]]
U = [[] for i in range(113+1) ]

for num, file in enumerate(['gTaxi.txt','gBus.txt','gMetro.txt'], start=0):
    with open(file) as f:
        for line in f:
            #print(dict(zip(*iter(line.split(':')))))
            ll = line.split(' ')
            for ii in range(len(ll)):
                if ii==0:
                    init = int(ll[ii])
                    continue
                if ll[ii]!='\n':
                    T[init][num].append(int(ll[ii]))
                    U[init].append([num,int(ll[ii])])
					
with open("mapasgraph.pickle", "wb") as fp:   #Pickling
    pickle.dump((T,U), fp)
					
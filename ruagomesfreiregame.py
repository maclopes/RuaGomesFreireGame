import math

d = {}
T = [ [[], [], [], []] for i in range(113+1) ]
T[0] = []

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

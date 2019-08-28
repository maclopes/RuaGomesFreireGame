import pickle
import matplotlib.pyplot as plt
from ruagomesfreiregame2sol import *

with open("coords.pickle", "rb") as fp:   # Unpickling
    coords = pickle.load(fp)
    
with open("mapasgraph.pickle", "rb") as fp:   #Unpickling
    AA = pickle.load(fp)
T = AA[0]
U = AA[1]

def plotpath(P,I,coords):
        img = plt.imread('maps.png')
        plt.imshow(img)
        colors = ['r.-','g+-','b^-']
        for agind in range(len(P[0])):
                st = I[agind]-1
                for ii in P:
                        nst = ii[agind][1]-1
                        plt.plot([coords[st][0],coords[nst][0]],[coords[st][1],coords[nst][1]],colors[agind])
                        st = nst
        plt.axis('off')
        plt.show()
        
def validatepath(P,I,T,LA=[20,10,5]):
	for ii in P:
		for agind,ag in enumerate(ii):
			st = I[agind]
			if LA[ag[0]]==0:
				if ag[1] != I[agind]:
					print('no more tickets')
					I = []
					return I
			else:
				LA[ag[0]] -= 1
				if ag[1] in T[st][ag[0]]:
					I[agind] = ag[1]
				else:
					print('invalid action')
					I = []
					return I
	return I

def validateplay(st,nst):
        return True

# (4 val) Exercise 1 - Get fixed ZeTelhado
st = [30, 40, 109, 57] # Guardas, ZeTelhado
st = [1, 2, 3, 105] # Guardas, ZeTelhado

ZeTelhado = ZeTelhado('fix',U,auxheur = coords)
SrGuarda = SrGuarda('smart1',U,auxheur = coords)
nturns = 15
while (st[3] not in st[0:3]) and (nturns>0):
        nst = [0,0,0,0]
        nst[3] = ZeTelhado.play(st)
        validateplay(st,nst[3])
        nst[0:3] = SrGuarda.play(st)
        validateplay(st,nst[0:3])
        nturns -= 1
        print(nst)
        st = nst

# (4 val) Exercise 2 - Get random ZeTelhado

# (4 val) Exercise 3 - Get smart ZeTelhado

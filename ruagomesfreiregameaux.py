I = [1,5,13]
P = [[[0,2],[1,6],[2,30]],[[0,3],[1,8],[2,60]],[[0,4],[1,9],[2,72]]]
plotpath(P,I,coords)

print('initial locations')
print(I)
I = validatepath(P,I,T)
print('final locations')
print(I)

I = [1,5,13]
P = [[[0,2],[1,6],[2,30]],[[0,3],[1,8],[2,60]],[[0,3],[1,9],[2,72]]]
print('initial locations')
print(I)
I = validatepath(P,I,T,LA=[2,5,5])
print('final locations')
print(I)

I = [1,5,13]
P = [[[0,2],[1,6],[2,30]],[[0,3],[1,8],[2,60]],[[0,4],[1,9],[2,72]]]
print('initial locations')
print(I)
I = validatepath(P,I,T,LA=[2,2,2])
print('final locations')
print(I)

I = [1,5,13]
P = [[[0,55],[1,6],[2,30]],[[0,3],[1,8],[2,60]],[[0,4],[1,9],[2,72]]]
print('initial locations')
print(I)
I = validatepath(P,I,T,LA=[2,2,2])
print('final locations')
print(I)

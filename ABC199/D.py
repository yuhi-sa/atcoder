import numpy as np

N,M = map(int,input().split())

Graph = np.zeros((M,M))
print(Graph)
for _ in range(M):
    a,b = map(int, input().split()) 
    Graph[a-1,b-1] = 1
    Graph[b-1,a-1] = 1

print(Graph)
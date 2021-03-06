import random as rdm 
import matplotlib.pyplot as plt
import networkx as nx 


def createNetwork(fileName):
    G = nx.read_edgelist(fileName,create_using=nx.DiGraph())
    return G



def Randomwalk(G):
    nodes=list(G.nodes())
    PageRank={}
    for i in range(len(nodes)):
        PageRank[ nodes[i] ]=0
    
    
    for i in range(10000):
     src=rdm.choice(nodes)
     PageRank[src]+=1 
     while(rdm.random()>0.2):
        if (len(list(G.neighbors(src)))==0):
            break
        else:
            dest=rdm.choice(list(G.neighbors(src)))
            PageRank[dest]+=1 
            src=dest 
    return PageRank
    
      
      
G=createNetwork("web-BerkStan.txt")

A=RandomWalk(G)
B=nx.pagerank(G)

List1=[]
List2=[]

nodes=list(G.nodes())


for n in nodes:
 List1.append(A[n])
 List2.append(B[n])

l=[]

for i in range (len(list1)):
    j=(float(list1[i])/sum(list1))
    l.append(j)

List1=l;

plt.plot(List1,List2)
plt.show()
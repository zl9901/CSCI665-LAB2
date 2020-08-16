
import sys
from random import randint

class GraphInputGenerator(object):
    def __init__(self,vertices,isWeighted,isDirected,adj,s):

        self.graph=[]
        self.set=s


        self.adj = adj
        self.vertices = vertices
        self.isWeighted = isWeighted
        self.isDirected = isDirected
        self.edges=vertices * (vertices - 1) / 2
        self.fillAdj()

    """
    fillAdj is the function which can determine the connectivity 
    of each node in the adjacency list 
    """
    def fillAdj(self):
        if self.set == 'set1':
            for v1 in range(self.vertices):
                count = 0
                while count < 9:
                    v2 = v1
                    while v2 == v1:
                        v2 = randint(0, self.vertices - 1)
                    if self.connectivity_check(v1) < 9 and self.connectivity_check(v2) < 9:
                        self.addEdge(v1, v2)
                    count += 1
        elif self.set == 'set2':
            for v1 in range(self.vertices):
                while self.connectivity_check(v1) < (self.vertices / 2):
                    v2 = v1
                    while v2 == v1:
                        v2 = randint(0, self.vertices - 1)
                    self.addEdge(v1, v2)
        else:
            count=0
            while count<self.edges:
                v1=randint(0,self.vertices-1)
                v2=v1
                while v2==v1:
                    v2=randint(0,self.vertices-1)
                if self.addEdge(v1,v2):
                    count+=1

    """
    connectivity_check function is used to 
    check the validity of node connectivity
    in adjacency list
    """
    def connectivity_check(self, v):
        count = 0
        for i in range(len(self.adj)):
            if i != v and self.adj[v][i] != 0:
                count += 1
        return count

    """
    the function of addEdge is designed to add edge in the 
    adjacency list
    """
    def addEdge(self,v1,v2):
        if self.adj[v1][v2]==0:
            e=1
            if self.isWeighted:
                e+=randint(0,int(self.edges*self.edges/2))
            self.adj[v1][v2]=e
            if not self.isDirected:
                self.adj[v2][v1]=e
            return True
        return False

    """
    print the adjacency list 
    """
    def genGraphInput(self):
        # print(str(self.vertices)+" "+str(self.edges))
        print("number of vertices are "+str(self.vertices))
        print()
        for i in range(0,len(self.adj)):
            for j in range(0 if self.isDirected else i,len(self.adj)):
                if self.adj[i][j]!=0:
                    var=" "
                    if  self.isWeighted:
                        var+=" "+str(self.adj[i][j])
                    array = []
                    array.append(i)
                    array.append(j)
                    array.append(int(var))
                    self.graph.append(array)

def main():
    v = int(sys.argv[1])
    s = sys.argv[2]

    adj = [[0 for x in range(v)] for y in range(v)]
    print("Weighted undirected graph:")
    g = GraphInputGenerator(v, True, False, adj,s)

    g.genGraphInput()
    print("Graph is shown as followed")
    print(g.graph)
    print()
    print("adjacency list is shown as followed")
    print(g.adj)

if __name__ == '__main__':
    main()
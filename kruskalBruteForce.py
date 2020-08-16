import time
import sys
from random import randint

class KruskalBruteForce(object):
    def __init__(self,vertices,isWeighted,isDirected,adj,s):

        self.graph=[]
        self.set=s

        self.visited=[]
        self.res=[]
        self.mark1=-1
        self.mark2=-1

        self.parent = []
        self.rank = []
        self.result=[]

        self.adj = adj
        self.vertices = vertices
        self.isWeighted = isWeighted
        self.isDirected = isDirected
        self.edges=vertices * (vertices - 1) / 2
        self.fillAdj()

    """
    BruteForce function is the algorithm without union and find 
    data structure, the time complexity is high
    """
    def BruteForce(self):
        e=0
        index=0
        while e<self.vertices and index<=self.vertices-1:
            if index==0:
                array=[]
                u = self.graph[index][0]
                v = self.graph[index][1]
                array.append(u)
                array.append(v)
                self.visited.append(array)
                self.res.append(self.graph[index])
                index+=1
                continue

            u=self.graph[index][0]
            v=self.graph[index][1]
            for i in range(0,len(self.visited)):
                for j in range(0,len(self.visited[i])):
                    if u==self.visited[i][j]:
                        self.mark1=i
                    if v==self.visited[i][j]:
                        self.mark2=i
            if self.mark1==-1 and self.mark2!=-1:
                self.visited[self.mark2].append(u)
                self.res.append(self.graph[index])
            elif self.mark1!=-1 and self.mark2==-1:
                self.visited[self.mark1].append(v)
                self.res.append(self.graph[index])
            elif self.mark1==-1 and self.mark2==-1:
                temp=[]
                temp.append(u)
                temp.append(v)
                self.visited.append(temp)
                self.res.append(self.graph[index])
            elif self.mark1!=-1 and self.mark2!=-1:
                if self.mark1!=self.mark2:
                    self.visited[self.mark1].extend(self.visited[self.mark2])
                    self.visited.pop(self.mark2)
                    self.res.append(self.graph[index])
            self.mark1=-1
            self.mark2=-1
            index+=1

    """
    find function is part of the union and find data structure
    which can return the specific index which is corresponding to 
    parent
    """
    def find(self,i):
        if self.parent[i]==i:
            return i
        else:
            return self.find(self.parent[i])

    """
    find function is part of the union and find data structure
    according to the array named rank
    it can change the value in array named parent
    """
    def union(self,x,y):
        if self.rank[x]==self.rank[y]:
            self.parent[y]=x
            self.rank[x]+=1
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
        elif self.rank[y]>self.rank[x]:
            self.parent[x]=y

    """
    main function which calls find function first and 
    then calls union function
    """
    def unionAndFind(self):
        index=0
        e=0
        for i in range(0,self.vertices):
            self.parent.append(i)
        for j in range(0,self.vertices):
            self.rank.append(0)
        while e<self.vertices and index<=self.vertices-1:
            u=self.graph[index][0]
            v=self.graph[index][1]
            x=self.find(u)
            y=self.find(v)
            if x!=y:
                e+=1
                xroot=self.find(x)
                yroot=self.find(y)
                self.union(xroot,yroot)
                self.result.append(self.graph[index])
            index += 1

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
    g = KruskalBruteForce(v, True, False, adj,s)

    g.genGraphInput()
    print("The unsorted graph is shown as followed")
    print(g.graph)
    print()
    g.graph=sorted(g.graph, key=lambda item: item[2])
    print("The sorted graph is shown as followed")
    print(g.graph)
    print()

    start=time.time()
    print("The order of MCST of my BruteForce algorithm is shown as followed")
    g.BruteForce()
    print(g.res)
    end=time.time()
    t = end - start
    print(" BruteForce time is ",t)

    print()

    start = time.time()
    g.unionAndFind()
    print("The order of MCST of union and find algorithm is shown as followed")
    print(g.result)
    end = time.time()
    t = end - start
    print(" UnionAndFind time is " ,t)


if __name__ == '__main__':
    main()
from collections import defaultdict


class Graph:
    def __init__(self):
        #   For storing vertices as key and
        #   the list of there connected vertices as value
        self.graph = defaultdict(list)
        #   For storing the tuple of two vertices
        #   as key and distance b/w them as value
        self.edges = defaultdict(list)
        #   For storing all the vertices as key and
        #   False as there default value
        self.visitedVer = defaultdict(list)
        #   For storing the vertices as key and
        #   there previous vertices as value with the shortes distance
        self.prev = defaultdict(list)
        #   For storing the vertices as key
        #   and distance from starting node as value
        self.minDistance = defaultdict(list)
        #   For storing all the vertices
        self.vertices = []

    #   Function for connecting two vertices or adding edge to the graph
    def addEdge(self,   u,
                v,  weight=1):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight
        #   Condition to check whether the same node is already present
        #   in the list or not
        if u not in self.vertices:
            self.vertices.append(u)
        #   Condition to check whether the same node is already present
        #   in the list or not
        if v not in self.vertices:
            self.vertices.append(v)

    #   Function to check whether the path exist between two nodes or not
    def pathExist(self, u, v):
        arr = []
        self.visited = defaultdict(list)
        for i in self.graph:
            self.visited[i] = False
        queue = []
        queue.append(u)
        self.visited[u] = True
        while queue:
            temp = queue.pop(0)
            #   Condition to check whether the dequeued vertex is equal
            #   to the destination vertex or not
            if temp == v:
                return True
            for i in self.graph[temp]:
                #   Condition to check whether the current vertex
                #  is already visited or not.
                if (self.visited[i] is False):
                    queue.append(i)
                    arr.append(temp)
                    self.visited[i] = True
        return False

    #   Function to find the shortest path from a point to all the nodes.
    def dijkstra(self, u):
        for i in self.vertices:
            self.visitedVer[i] = False
        for i in self.vertices:
            #   Condition to check if the vertex present in vertices list
            #   is equals to starting node or not.
            #   if the condition is true its minimum distance is assign as 0
            if i == u:
                self.minDistance[(u, i)] = 0
            else:
                #   else the minimum distance is set as infinite
                #   or a very large value say 10**9
                self.minDistance[(u, i)] = 10**9
        temp = u
        while (self.visitedVer[temp] is False):
            self.visitedVer[temp] = True
            for i in self.graph[temp]:
                if (self.visitedVer[i] is False and
                        self.minDistance[(u, i)] > self.edges[(temp, i)]
                        + self.minDistance[(u, temp)]):
                    #   Condtion to check whether the vertex is
                    #   already visited or not and to check whether
                    #   the distance between adjacent node of current
                    #   node and starting is greater then the sum of
                    #   distace from starting node to current node and
                    #   adjacent node of currnet node
                    self.minDistance[(u, i)] = self.edges[(temp, i)]
                    + self.minDistance[(u, temp)]
                    self.prev[i] = temp
            largest = 10**9
            for i in self.graph:
                if (self.visitedVer[i] is False and
                        self.minDistance[(u, i)] < largest):
                    #   Condition to check for those unvisited vertices
                    #   whose distance is updated from infinite but
                    #   that is not the shortest distance from the
                    #   starting vertex
                    largest = self.minDistance[(u, i)]
                    temp = i
        return self.prev

    #   Function to find the shortest distance from source to destination
    def sourceToDest(self, u, v):
        if self.pathExist(u, v):
            #   Condition to check whether the path exist
            #   between source and destination or not
            prev = self.dijkstra(u)
            #   Creating a list of all the vertices
            #   connecting form source to previous element of dest.
            prev = list(prev.items())
            sourceToDest = []
            temp = v
            while temp:
                sourceToDest.insert(0, temp)
                # Condition to check whether the current vertex
                #  is source or not
                if (temp == u):
                    break
                for i in range(len(prev)):
                    #   Conditon to check if the verext at position 0 is
                    #   equals to destination or not.
                    #   if yes then temp is assign to its previous vertex
                    if (prev[i][0] == temp):
                        temp = prev[i][1]
            sourceToDest = set(sourceToDest)
            return sourceToDest
        return -1

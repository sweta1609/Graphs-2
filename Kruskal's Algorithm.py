class Edge:
    def __init__(self,src,dest,weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        
def getParent(v,parent):
    if (v == parent[v]):
        return v
    return getParent(parent[v],parent)

def kruskal(edges , nVertices):
    parent = [i for i in range (nVertices)] #parent array is formed where ex- 0 will be parent of 0 ,1 will be parent of 1
    edges = sorted(edges,key=lambda edge:edge.weight) #sorting of array ,lambda gives access to the object and propertiesof object
    count = 0 #we will maintain count
    output = []
    i = 0
    while count <(nVertices-1):
        currentEdge = edges[i]
        srcparent = getParent(currentEdge.src,parent)
        destparent = getParent(currentEdge.dest,parent)
        
        if srcparent != destparent:
            output.append(currentEdge)
            count += 1
            parent[srcparent] =  destparent
        i += 1
    return output

 #taking input       
li = [int(ele) for ele in input().split()]
n = li[0] #no. of vertices
E = li[1] #no. of edges
edges = [] #edges array
        
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    weight = curr_input[2]
    edge = Edge(src,dest,weight)
    edges.append(edge) #append edge in list
output = kruskal(edges,n) #kruskal will take edges and vertices as input


for edge in output: #for printing output ,here v1 should always be less then v2 and it will print v1,v2, and weight
    if edge.src < edge.dest:
        print(str(edge.src)+" " + str(edge.dest)+" "+ str(edge.weight))
    else:
        print(str(edge.dest)+" " + str(edge.src)+" "+ str(edge.weight))
        
        
    

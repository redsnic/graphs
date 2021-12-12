from graphs.Graph import Graph
from graphs.Node import Node 
 
if __name__=="__main__": 

    G = Graph()
    
    nodes = {}
    nodes["A"] = Node("A") 
    nodes["B"] = Node("B") 
    nodes["C"] = Node("C")

    for node in nodes.values():
        G.add(node)

    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(0,2)

    print(nodes["A"].indegree())
    print(nodes["A"].outdegree())

    print(G)

    G.remove(1)

    print(G) 

    G.add(nodes["B"])

    print(G)

    G.add_edge(1,2)

    print(G.distance(0,2))

    



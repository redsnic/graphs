import numpy as np

class Graph():

    def __init__(self):
        """ Default constructor

        Creates an empty graph
        """    
        # the graph is here implemented as a list of nodes
        self.nodes = []
    
    def add(self, node):
    
        """ Add a node to this graph

        complexity: O(1)
    
        :type node: Node object
        :param node: The node to be added
    
        :rtype: integer
        :return: the id of this newly added node in the graph
    
        NOTE: node id may change if other operations are done on the graph.
              Referring to the node "id" field is a safer option
        NOTE: node objects must be different when added, no copy is done
              to lower complexity costs
        """
        node.id=len(self.nodes)
        self.nodes.append(node)
        return node.id

    def remove(self, index):
        """ Remove a node from this graph
        
        This includes node and edge deletions, node ids are modified accordingly

        complexity: O(|V|+|E|)

        :type index: integer
        :param index: index of the node to be removed. REQUIRES: 0 <= index < |V|

        """

        assert 0 <= index < len(self.nodes), "Node index out of range [0, " + str(len(self.nodes)) + ") : " + str(index)

        # remove edges
        for j in list(self.nodes[index].edges_out):
            self.remove_edge(index,j)
        for j in list(self.nodes[index].edges_in):
            self.remove_edge(j,index)

        # update indexes
        for i in range(len(self.nodes)):
            self.nodes[i].id = self.nodes[i].id - (1 if index<=i else 0)
            self.nodes[i].edges_in  = set([ j - (1 if index<=j else 0) for j in self.nodes[i].edges_in])
            self.nodes[i].edges_out = set([ j - (1 if index<=j else 0) for j in self.nodes[i].edges_out])

        # remove nodes
        del self.nodes[index]

    def add_edge(self, i, j):
        """ Add an edge to this graph

        complexity: O(1)

        :type i: integer
        :param i: index of the source. REQUIRES: 0 <= index < |V|

        :type j: integer
        :param j: index of the destination. REQUIRES: 0 <= index < |V|

        """
        assert 0 <= i < len(self.nodes), "Node index out of range (i) [0, " + str(len(self.nodes)) + ") : " + str(i)
        assert 0 <= j < len(self.nodes), "Node index out of range (j) [0, " + str(len(self.nodes)) + ") : " + str(j)
        self.nodes[i]._add_edge_out(j)
        self.nodes[j]._add_edge_in(i)

    def remove_edge(self, i, j):
        """ Remove an edge from this graph

        complexity: O(1)

        :type i: integer
        :param i: index of the source. REQUIRES: 0 <= index < |V|

        :type j: integer
        :param j: index of the destination. REQUIRES: 0 <= index < |V|

        """
        assert 0 <= i < len(self.nodes), "Node index out of range (i) [0, " + str(len(self.nodes)) + ") : " + str(i)
        assert 0 <= j < len(self.nodes), "Node index out of range (j) [0, " + str(len(self.nodes)) + ") : " + str(j)
        self.nodes[i]._remove_edge_out(j)
        self.nodes[j]._remove_edge_in(i)

    def adj(self):
        """ Get adjacency matrix

        complexity: O(|V|^2)

        :rtype: numpy matrix
        :return: A numpy matrix representing the adjacency matrix of this graph. Indexes are consistent.

        """
        mat = []
        for i in range(len(self.nodes)):
            line = [ 0 for _ in self.nodes ]
            for j in self.nodes[i].edges_out:
                line[j] = 1
            mat.append(line)
        return np.matrix(mat)

    def adj_list(self):
        """ Get adjacency list

        complexity: O(|V|+|E|)

        :rtype: [[integer]]
        :return: The adjacency list of this graph. Indexes are consistent.

        """
        return [ list(self.nodes[i].edges_out) for i in range(len(self.nodes)) ]
        
    def n(self):
        """ Number of nodes

        complexity: O(1)

        :rtype: integer
        :return: |V|

        """
        return len(self.nodes)

    def distance(self, i, j):
        """ Compute distance between two nodes

        complexity = O(|V|+|E|)

        :type i: integer
        :param i: index of the source. REQUIRES: 0 <= index < |V|

        :type j: integer
        :param j: index of the destination. REQUIRES: 0 <= index < |V|

        :rtype: integer
        :return: distance if i and j are reachable, -1 otherwise

        """
        assert 0 <= i < len(self.nodes), "Node index out of range (i) [0, " + str(len(self.nodes)) + ") : " + str(i)
        assert 0 <= j < len(self.nodes), "Node index out of range (j) [0, " + str(len(self.nodes)) + ") : " + str(j)

        # BFS algorithm
        visited = [ False for _ in self.nodes ]
        active = [i]
        visited[i] = True

        
        for distance in range(len(self.nodes)):
            # check if visited
            if visited[j] == 1:
                return distance

            # maximum distance is |V| (by pumping lemma)
            if distance == len(self.nodes)-1:
                break
            
            # core algorithm
            next_active = []
            for current in active:
                for destination in self.nodes[current].edges_out:
                    if not visited[destination]:
                        # a node is never inserted twice in active list
                        next_active.append(destination) 
                        visited[destination] = True

            active = next_active

        return -1

    def __str__(self):
        """ Print this graph in graphviz format

        NOTE: nodes must be printable (have __str__ method)
        """
        out = "digraph G {\n"
        for node in self.nodes:
            out += str(node.id) + " [label=" + str(node.get()) + "]\n"
        for node in self.nodes:
            i = node.id
            for j in node.edges_out:
                out += str(i) + " -> " + str(j) + "\n"
        out += "}\n"
        return out

    



class Node():
    """
    General class to manage very simple nodes in graphs
    """

    def __init__(self, content):
        """ Default constructor
        
        encapsulates an object of any kind in a Node (a graph node). 
        Node objects are meant to be used with the Graph class
    
        :type content: any  
        :param content: the content of the node (aka: label) 
    
        """    
        self.content = content
        self.edges_in = set()
        self.edges_out = set()
        self.id = None

    def get(self):
        """ Get node content

        :rtype: any
        :return: the node content
        """
        return self.content 

    def set(self, content):
        """ Set node content
    
        :type content: any
        :param content: the content of the node (aka: label) 

        """    
        self.content = content

    def indegree(self):
        """ Get the indegree of this node

        the indegree is defined as the number of edges entering this node
    
        :rtype: integer
        :return: the indegree of this node
        """
        return len(self.edges_in)

    def outdegree(self):
        """ Get the outdegree of this node

        the outdegree is defined as the number of edges exiting this node
    
        :rtype: integer
        :return: the outdegree of this node
        """
        return len(self.edges_out)

    def _add_edge_in(self, index):
        """ Add an edge entering in this node
    
        :type index: integer
        :param index: the id of the connected node

        """    
        self.edges_in.add(index)

    def _add_edge_out(self, index):
        """ Add an edge exiting this node
    
        :type index: integer
        :param index: the id of the connected node

        """  
        self.edges_out.add(index)

    def _remove_edge_in(self, index):
        """ Remove an edge entering in this node
    
        :type index: integer
        :param index: the id od the connected node

        """  
        self.edges_in.remove(index)

    def _remove_edge_out(self, index):
        """ Remove an edge exiting this node
    
        :type index: integer
        :param index: the id od the connected node

        """  
        self.edges_out.remove(index)

    
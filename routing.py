# File: routing.py

"""
This module defines a routing table for the ARPANET routing assignment.
Your job in this assignment is to implement the RoutingTable class so
its methods implement the functionality described in the comments.
"""

class RoutingTable:

    """
    This class implements a routing table, which keeps track of
    two data values for each destination node discovered so far:
    (1) the hop count between this node and the destination, and
    (2) the name of the first node along the minimal path.
    """

    def __init__(self, name):
        """
        Creates a new routing table with a single entry indicating
        that this node can reach itself in zero hops.
        """
        self.name = name
       	self.hop_table = {self.name: 0}
       	self.neighbors = {}

    def getNodeNames(self):
        """
        Returns an alphabetized list of the known destination nodes.
        """
       	node_name_list = list(self.hop_table.keys())
       	node_name_list.sort()
       	return node_name_list

    def getHopCount(self, destination):
        """
        Returns the hop count from this node to the destination node.
        """
        if destination in self.hop_table:
        	return self.hop_table[destination]
        else:
        	return None

    def getBestLink(self, destination):
        """
        Returns the name of the first node on the path to destination.
        """
        best_table = self
        best_node = self.name
        hop_tables = self.neighbors.items()
        for node_name,hop_table in hop_tables:
        	candidate = hop_table.getHopCount(destination)
        	current_best = best_table.getHopCount(destination)
        	if candidate <= current_best:
        		best_node = node_name
        		best_table = hop_table
        return best_node


    def update(self, source, table):
        """
        Updates this routing table based on the routing message just
        received from the node whose name is given by source.  The table
        parameter is the current RoutingTable object for the source.
        """
       	hop_counts = table.hop_table.items()
       	for node_name,node_distance in hop_counts:
       		if node_name != self.name:
	       		if node_name in self.hop_table:
	       			if self.getHopCount(node_name) > node_distance:
	       				self.hop_table[node_name] = node_distance + 1
	       		else:
	       			self.hop_table[node_name] = node_distance + 1
	       		if node_distance + 1 == 1:
	       			if node_name not in self.neighbors:
	       				if node_name == source:
	       					self.neighbors[node_name] = table
      

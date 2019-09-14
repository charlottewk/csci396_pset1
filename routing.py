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
        # You complete this implementation

    def getNodeNames(self):
        """
        Returns an alphabetized list of the known destination nodes.
        """
        # You complete this implementation

    def getHopCount(self, destination):
        """
        Returns the hop count from this node to the destination node.
        """
        # You complete this implementation

    def getBestLink(self, destination):
        """
        Returns the name of the first node on the path to destination.
        """
        # You complete this implementation

    def update(self, source, table):
        """
        Updates this routing table based on the routing message just
        received from the node whose name is given by source.  The table
        parameter is the current RoutingTable object for the source.
        """
        # You complete this implementation
      

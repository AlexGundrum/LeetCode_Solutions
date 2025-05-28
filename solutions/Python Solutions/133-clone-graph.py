'''
https://leetcode.com/problems/clone-graph/description/


Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
idea: go thru all of nodes once to create the new node of same val
have map map val --> node mem location

then loop thru a second time, setting the newnode's neighbors 

map can map val --> node bc our nodes are enumerated 1-n, unique vals. 

'''

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        valToNodeMap = dict()
        #cur = node
        q = deque()
        if node:
            q.append(node)
        
        while q:
            for i in range(len(q)):
                curnode = q.popleft()
                newnode = Node(curnode.val)
                valToNodeMap[newnode.val] = newnode
                for neighbor in curnode.neighbors:
                    if neighbor.val not in valToNodeMap:
                        q.append(neighbor)
        
        
        hasNeighborsSet = set()
        q.append(node)
        while q:
            for i in range(len(q)):
                curnode = q.popleft()
                newnode = valToNodeMap[curnode.val]
                hasNeighborsSet.add(newnode.val)
                if curnode.neighbors is not None:
                    newnode.neighbors = []
                    for neighbor in curnode.neighbors:
                        if not (neighbor.val in hasNeighborsSet):
                            q.append(neighbor)
                        newnode.neighbors.append(valToNodeMap[neighbor.val])

        return valToNodeMap[1]









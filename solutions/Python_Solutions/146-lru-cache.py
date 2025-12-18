'''


https://leetcode.com/problems/lru-cache/description/


Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity'''


class LRUCache:
    #dll that is our "priority" that keeps track of LRU
    #have hash map that takes value, points to where in dll it is.
    #this allows us to update priority in constant time

    #put:  
    #   1) check if its already in our DLL and hash map. if so, update val, move to front of dll
    #   2) if not, see if we have to kill last node in dll - remove from dll & hashmap
    #   3) make new node, add to front of dll, add to hash map

    #get: 
    #   1) check if its in hash map, if so, return val, move to front of dll
    #   2) if not, return -1
    class Node:
        def __init__(self, val, key):
            self.val = val
            self.key = key
            self.nextPtr = self
            self.prevPtr = self
    
    def __init__(self, capacity: int):
        self.keyToNodeMap = dict()
        self.head = None
        #self.tail = None
        self.capacity = capacity
    def printDLL(self):
        cur = self.head
        #print("Nodes in DLL: ")
        numsPrinted = set()
        while cur and cur.key not in numsPrinted: 
            #print(str(cur.key), end=", ")
            numsPrinted.add(cur.key)
            cur = cur.nextPtr
        #print(" ")
    
    def moveNodeToFront(self, node):
        if self.head is not None:
            last, second = self.head.prevPtr, self.head
            last.nextPtr = node
            second.prevPtr = node
            node.nextPtr = second
            node.prevPtr = last
            self.head = node
        else:
            self.head = node
    
    def removeNodeFromLL(self, node):
        if self.head == node and node.nextPtr != node:
            newPrev = self.head.prevPtr
            self.head = self.head.nextPtr
            self.head.prevPtr = newPrev
            return
        elif self.head == node and node.nextPtr == node:
            self.head = None
            return
        
        node.prevPtr.nextPtr = node.nextPtr
        node.nextPtr.prevPtr = node.prevPtr
        

    
    def get(self, key: int) -> int:
        #print("before get: " )
        #self.printDLL()
        if key in self.keyToNodeMap:
            node = self.keyToNodeMap[key]
            self.removeNodeFromLL(node)
            self.moveNodeToFront(node)
            return node.val
            #print("after get: ")
            #self.printDLL()
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        #print("Put: " + str(key) + " with val: " + str(value))
        #print("Keys in map: " + str(self.keyToNodeMap.keys()))
        #self.printDLL()
        if key in self.keyToNodeMap.keys():
            #key is already in our cache, update value (redundant if not changing val, but thats ok)
            #print(str(key) + " is already in map")
            node = self.keyToNodeMap[key]
            node.val = value
            self.removeNodeFromLL(node)
            self.moveNodeToFront(node)
            #self.printDLL()
            return

        elif len(self.keyToNodeMap.keys()) == self.capacity:
            
            #kill tail from dll, AND hashmap
            toKill = self.head.prevPtr
            self.removeNodeFromLL(toKill)
            
            self.keyToNodeMap.pop(toKill.key)
            #print("Killing : " + str(toKill.key))
            #self.printDLL()
        
        #create new node, add it to hashmap, move to front
        #print("creating and adding: " + str(key) + " to the front")
        node = LRUCache.Node(value, key)
        self.keyToNodeMap[key] = node
        self.moveNodeToFront(node)
        #print("Keys in map: " + str(self.keyToNodeMap.keys()))
        #self.printDLL()











#link nodes(cargo payload + pointer to neighbor) into lists
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    #while a list contains nodes print cargo and increment
    def printList(node):
        while node:
            print node,
            node = node.next
        print

    def printBackward(self):
        if self.next != None:
            tail = self.next
            tail.printBackward()
        print self.cargo,

class LinkedList :
    def __init__(self) :
        self.length = 0
        self.head = None

    def printBackward(self):
        print "[",
        if self.head != None:
            self.head.printBackward()
            print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1



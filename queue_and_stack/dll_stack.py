import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size+=1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size-= 1
            self.storage.remove_from_tail()

    def len(self):
        return self.size

    '''
        how to traverse a linked list without a tail
        current_node = self.head
        while curret_node.next is not None:
            if current_node.next is None:
                self.tail is current_node
            current_node = current_node.next

    '''

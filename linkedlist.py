from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def contains_node(self, data):
        node = self.head
        position = 1
        results = []
        while node is not None:
            if node.contains_data(data):
                results.append(position)

            node = node.next
            position = position + 1

        if results:
            print(f'This node is located at position {results} in the list')
        else:
            print('This node was not found!')
        return results

    def add_to_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

        #temporary_node = self.head

        #while temporary_node.next is not None:
            #temporary_node = temporary_node.next

        #temporary_node.next = node
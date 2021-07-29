
# Each member has a value and a tail pointer
# Each member will be a class object

class Node(object):
    def __init__(self, value):
        self.value = value
        self.tail = None


class LinkedList(object):
    def __init__(self):
        self.linked_head = None
        self.linked_tail = None

    def add_node(self, value):
        # Initialize a new linked list member
        node = Node(value)

        if self.linked_head is None:
            # Initial condition
            self.linked_head = node
            self.linked_tail = node
        else:
            # Link new node to the last node
            self.linked_tail.tail = node
            self.linked_tail = node

    def print(self):
        if self.linked_head is None:
            print('Linked list is empty!')
        else:
            curr_node = self.linked_head
            while True:
                print(curr_node.value)
                if curr_node.tail is None:
                    break
                else:
                    curr_node = curr_node.tail

    def add_node_at_head(self):
        pass

    def remove_node(self, value):
        pass

    def length(self):
        pass

    def add_node_at_index(self, index):
        pass

    def remove_node_at_index(self, index):
        pass

    def search(self, value):
        pass


linked_list = LinkedList()
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
linked_list.add_node(7)

linked_list.print()

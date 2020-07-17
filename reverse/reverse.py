class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is not None:
            # Store the next node in the LL
            next = node.next_node
            # Set the node's next node to prev
            node.next_node = prev
            # Recursive - pass in the new current node(next node) and new prev node(current node)
            self.reverse_list(next, node)
        # If the passed in node is None, we've reached the end of the LL, set head to prev
        else:
            self.head = prev

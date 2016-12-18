"""Create a Double Linked List Data Structure."""


class Dbl_Node(object):
    """Create Node objects for use in a Linked List data structure.

    Attributes:
        value:      A value or data stored in the Node.
        nxt:        Pointer to the next Node.
        prev:       A pointer to a previus Node.
    """

    def __init__(self, value=None, nxt=None, prev=None):
        """Initialize a Node type object."""
        self.value = value
        self.nxt = nxt
        self.prev = prev


class Dbl_Linked_List(object):
    """Double Linked List (DLL) style Data Structure.

    If initialized with an iterable, will create nodes for each item in
    the iterable.

    Attributes:
        head:       Node on one end of DLL, last item added if
                    initialized with iterable.
        tail:       Node on other end of DLL, first item added if
                    intailized with iterable.
        _size:      The length of the DLL or number of Nodes stored
                    in the list.

    Methods:
        push(value):    Given a value, add a new Node object to the DLL.

        append(value):  Given a value, adds it at the end of the line.

        pop():          Pop the head Node off the list, return the value.

        shift():        will remove the last value from the line and return it.

        remove(val):    Given a Node, remove that Node from the Linked List.
                        Else, raise a ValueError.
    """

    def __init__(self, maybe_an_iterable=None):
        """Intialize a Double Linked List Object."""
        self.head = None
        self.tail = None
        self._size = 0
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
                nodes = [node for node in self._iterate_from(self.head)]
                self.tail = nodes[-1]
            except TypeError:
                self.push(maybe_an_iterable)

    def push(self, value):
        """Add a node at the beginning of list and reassign head."""
        new = Dbl_Node(value)
        if self._size > 0:
            old = self.head
            self.head = new
            new.nxt = old
            old.prev = new
        else:
            self.head = new
            self.tail = self.head
        self._size += 1

    def pop(self):
        """Remove head node from DLL and return its value."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty Double Linked List.")
        val = self.head.value
        if self._size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nxt
            self.head.prev = None
        self._size -= 1
        return val

    def shift(self):
        """Remove tail node from DLL and return its value."""
        if self.tail is None:
            raise IndexError("Cannot shift from an empty Double Linked List.")
        val = self.head.value
        if self._size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.nxt = None
        self._size -= 1
        return val

    def append(self, value):
        """Append a new node at the end of list and reassign tail."""
        new = Dbl_Node(value)
        if self._size > 0:
            old = self.tail
            self.tail = new
            new.prev = old
            old.nxt = new
        else:
            self.tail = new
            self.head = self.tail
        self._size += 1

    def remove(self, value):
        """Remove the given node from the DLL."""
        r_node = [node for node in self._iterate_from(self.head) if node.value == value]
        if not r_node:
            raise ValueError("ERROR: That node is not in this linked list.")
        for node in self._iterate_from(self.head):
            if r_node[0].value == node.value:
                if self.head.value == r_node[0].value:
                    self.pop()
                    return "Succesfully removed Node with value: {0}. New head set to {1}".format(r_node[0].value, self.head.value)
                elif node.nxt is None:
                    self.shift()
                    return "Succesfully removed Node with value: {} using Shift()".format(r_node[0].value)
                else:
                    r_node[0].prev.nxt = r_node[0].nxt
                    r_node[0].nxt.prev = r_node[0].prev
                    self._size -= 1
                    return "Succesfully removed Node with value: {}".format(r_node[0].value)

    def _iterate_from(self, list_item):
        """Return a generator."""
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt

    def __len__(self):
        """Return _size of DLL."""
        return self._size

class Node:

    def __init__(self, item=None):
        self.item = item
        self.nextNode: Node = None
        self.prevNode: Node = None


class LinkedList:

    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self._count: int = 0
        self.clear()

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return self.toString()

    def __contains__(self, item) -> bool:
        return self.hasElement(item)

    def __copy__(self):
        return self.clone()

    def __getitem__(self, index: int):
        return self.get(index=index)

    def __setitem__(self, index: int, item):
        """Please, do not use this. It is full of bugs. I do not know why, but somehow it adds the item at given index"""
        self.set(index=index, item=item)

    def clone(self):
        c = LinkedList()
        x = self.first
        while x is not None:
            c.addBack(x)
            x = x.nextNode
        return c

    def length(self) -> int:
        return self._count

    def count(self) -> int:
        return self._count

    def _checkElementIndex(self, index: int):
        if not self._isElementIndex(index):
            raise IndexError()

    def _checkPositionIndex(self, index: int):
        if not self._isPositionIndex(index):
            raise IndexError()

    def _isElementIndex(self, index: int) -> bool:
        """Tells if the argument is the index of an existing element"""
        return 0 <= index < self._count

    def _isPositionIndex(self, index: int) -> bool:
        """Tells if the argument is the index of a valid position for an iterator or an add operation"""
        return 0 <= index <= self._count

    def _linkFirst(self, item):
        f: Node = self.first
        newNode: Node = Node(item)
        newNode.nextNode = f
        self.first = newNode
        if f is None:
            self.last = newNode
        else:
            f.prevNode = newNode
        self._count += 1

    def _linkLast(self, item):
        l: Node = self.last
        newNode: Node = Node(item)
        newNode.prevNode = l
        self.last = newNode
        if l is None:
            self.first = newNode
        else:
            l.nextNode = newNode
        self._count += 1

    def _linkBefore(self, item, succ: Node):
        assert succ is not None
        pred: Node = succ.prevNode
        newNode: Node = Node(item)
        newNode.prevNode = pred
        newNode.nextNode = succ
        succ.prevNode = newNode
        if pred is None:
            self.first = newNode
        else:
            pred.nextNode = newNode
        self._count += 1

    def _unlinkFront(self, f: Node):
        assert f == self.first and f is not None
        element = f.item
        next: Node = f.nextNode
        f.item = None
        f.nextNode = None
        del f.item
        del f.nextNode
        del f
        self.first = next
        if next is None:
            self.last = None
        else:
            next.prevNode = None
        self._count -= 1
        return element

    def _unlinkBack(self, l: Node):
        assert l == self.last and l is not None
        element = l.item
        prev: Node = l.prevNode
        l.item = None
        l.prevNode = None
        del l.item
        del l.prevNode
        del l
        self.last = prev
        if prev is None:
            self.first = None
        else:
            prev.nextNode = None
        self._count -= 1
        return element

    def _unlink(self, x: Node):
        assert x is not None
        element = x.item
        next: Node = x.nextNode
        prev: Node = x.prevNode
        if prev is None:
            self.first = next
        else:
            prev.nextNode = next
            x.prevNode = None
        if next is None:
            self.last = prev
        else:
            next.prevNode = prev
            x.nextNode = None
        x.item = None
        self._count -= 1
        return element

    def _node(self, index: int) -> Node:
        """Returns the (non-None) Node at the specified index"""
        assert self._isElementIndex(index)

        if index < (self._count >> 1):
            x: Node = self.first
            for i in range(0, index, 1):
                x = x.nextNode
            return x
        x: Node = self.last
        for i in range(self._count - 1, index, -1):
            x = x.prevNode
        return x

    def add(self, index: int, item):
        """
        :param index: If this is None, then the item will be added as the last item
        :param item: The item to be added
        :return: Nothing
        """
        if index is None:
            self._linkLast(item)
            return
        # imitate python's way to get elements
        # e.g. grab 2nd-last item with -2
        if index >= self._count or index <= -self._count:
            raise IndexError()
        if index < 0:
            index = self._count - index
        self._checkPositionIndex(index)
        if index == self._count:
            self._linkLast(item)
        else:
            self._linkBefore(item, self._node(index))

    def addBack(self, item):
        self._linkLast(item)

    def addFront(self, item):
        self._linkFirst(item)

    def remove(self, item=None, index: int = None) -> Node:
        """Removes a specified element in different cases
        If item is None and index is given, the element at the specified position will be removed.
        If item is given and index is None, the first occurrence of the element will be removed.
        If item is None and index is None, the first occurrence of a None-element will be removed.
        If item is given and index is given, the first occurrence of the element, starting with the specified position,
            will be removed.
        :returns The removed element. None if no element was removed
        """
        if index is not None and item is None:
            self._checkElementIndex(index)
            return self._unlink(self._node(index))
        elif item is None and index is None:
            x: Node = self.first
            while x is not None:
                if x.item is None:
                    return self._unlink(x)
                x = x.nextNode
        elif item is not None and index is None:
            x: Node = self.first
            while x is not None:
                # We want to compare equality of the element, not the address
                if item == x.item:
                    return self._unlink(x)
                x = x.nextNode
        else:
            self._checkPositionIndex(index)
            x: Node = self.first
            currIndex = 0
            while x is not None and currIndex != index:
                # first get to the starting index
                x = x.nextNode
                currIndex += 1
            while x is not None:
                # then find the first occurrence of given element
                # and remove it
                if item == x.item:
                    return self._unlink(x)
                x = x.nextNode
        return None

    def removeBack(self):
        f: Node = self.last
        if f is None:
            raise AttributeError()
        return self._unlinkBack(f)

    def removeFront(self):
        f: Node = self.first
        if f is None:
            raise AttributeError()
        return self._unlinkFront(f)

    def removeFirst(self):
        return self.removeFront()

    def removeLast(self):
        return self.removeBack()

    def getFront(self):
        f = self.first
        if f is None:
            raise AttributeError()
        return f.item

    def getBack(self):
        l = self.last
        if l is None:
            raise AttributeError()
        return l.item

    def get(self, index: int):
        # imitate python's way to get elements
        # e.g. grab 2nd-last item with -2
        if index >= self._count or index <= -self._count:
            raise IndexError()
        if index < 0:
            index = self._count + index
        self._checkElementIndex(index)
        return self._node(index).item

    def set(self, index: int, item):
        # imitate python's way to get elements
        # e.g. grab 2nd-last item with -2
        if index >= self._count or index <= -self._count:
            raise IndexError()
        if index < 0:
            index = self._count + index
        self._checkElementIndex(index)
        x: Node = self._node(index)
        oldVal = x.item
        x.item = item
        return oldVal

    def hasElement(self, item) -> bool:
        return self.indexOf(item) >= 0

    def indexOf(self, item) -> int:
        index = 0
        if item is None:
            x: Node = self.first
            while x is not None:
                if x.item is None:
                    return index
                x = x.nextNode
                index += 1
        else:
            x: Node = self.first
            while x is not None:
                if x.item == item:
                    return index
                x = x.nextNode
                index += 1
        return -1

    def lastIndexOf(self, item) -> int:
        index = self._count
        if item is None:
            x: Node = self.last
            while x is not None:
                index -= 1
                if x.item is None:
                    return index
                x = x.prevNode
        else:
            x: Node = self.last
            while x is not None:
                index -= 1
                if x.item == item:
                    return index
                x = x.prevNode
        return -1

    def push(self, item):
        """Pushes an element into the front"""
        self.addFront(item)

    def pushBack(self, item):
        """Pushes an element onto the back"""
        self.addBack(item)

    def pop(self):
        """Pops the last element and returns it"""
        return self.removeLast()

    def popFront(self):
        """Pops the first element and returns it"""
        return self.removeFront()

    def enqueue(self, item):
        """Adds an element into the front of the queue"""
        self.addFront(item)

    def dequeue(self):
        """Removes an element from the back of the queue and returns it"""
        return self.removeBack().item

    def clear(self):
        x: Node = self.first
        while x is not None:
            next: Node = x.nextNode
            x.item = None
            x.nextNode = None
            x.prevNode = None
            del x.item
            del x.nextNode
            del x.prevNode
            x = next
        self.first = self.last = None
        self._count = 0

    def toPythonList(self) -> list:
        l = []
        currNode = self.first
        while currNode is not None:
            l.append(currNode.item)
            currNode = currNode.nextNode
        return l

    @classmethod
    def fromPythonList(cls, l: list):
        b = LinkedList()
        for i in range(0, len(l), 1):
            b.addBack(item=l[i])
        return b

    def reverse(self):
        l = self.toPythonList()
        self.clear()
        for i in range(0, len(l), 1):
            self.addFront(l[i])
        del l

    def toString(self) -> str:
        currNode = self.first
        string = '['
        if currNode is None:
            return string + ']'
        string = string + str(currNode.item)
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
            string = string + ", " + str(currNode.item)
        return string + ']'

    def sortAsc(self):
        front = self.first
        back = None
        while front is not None:
            back = front.nextNode
            while back is not None and back.prevNode is not None and back.item < back.prevNode.item:
                t = back.item
                back.item = back.prevNode.item
                back.prevNode.item = t
                back = back.prevNode
            front = front.nextNode

    def sortDesc(self):
        front = self.first
        back = None
        while front is not None:
            back = front.nextNode
            while back is not None and back.prevNode is not None and back.item > back.prevNode.item:
                t = back.item
                back.item = back.prevNode.item
                back.prevNode.item = back.item
                back = back.prevNode
            front = front.nextNode
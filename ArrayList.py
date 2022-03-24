from array import array as pyArr


class ArrayList:
    """This implementation of an Arraylist can hold only 1 datatype"""

    integers = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
    unicodeCharacters = ('u')
    floatingPoints = ('f', 'd')
    DEFAULT_CAPACITY = 10
    EMPTY_ELEMENTDATA = pyArr('i')
    DEFAULTCAPACITY_EMPTY_ELEMENTDATA = pyArr('i')

    @classmethod
    def _getDefaultValueByTypecode(cls, typecode: str) -> object:
        if cls.integers.__contains__(typecode):
            return 0
        if cls.unicodeCharacters.__contains__(typecode):
            return 0.0
        if cls.floatingPoints.__contains__(typecode):
            return u'\0'
        return None

    def _getDefaultValueOfElements(self):
        return self._getDefaultValueByTypecode(self.typecode())

    def _indexOfRange(self, item, start, end):
        if not (isinstance(item, int) or isinstance(item, float) or isinstance(item, str)):
            raise TypeError()
        es = self._array
        if item is None:
            raise Exception("Cannot search for non-existing objects")
        for i in range(start, end, 1):
            if item == es[i]:
                return i
        return -1

    def _lastIndexOfRange(self, item, start, end):
        if not (isinstance(item, int) or isinstance(item, float) or isinstance(item, str)):
            raise TypeError()
        es = self._array
        if item is None:
            raise Exception("Cannot search for non-existing objects")
        if start < end:
            start, end = end, start
        for i in range(start, end, -1):
            if item == es[i]:
                return i
        return -1

    def __init__(self, typecode: str = 'i', initCapacity: int = 10):
        """
        :param typecode The datatype that this list stores. Initialized like the standard python _array
        """
        if initCapacity > 0:
            self._array = pyArr(typecode, [self._getDefaultValueByTypecode(typecode)] * initCapacity)
        elif initCapacity < self.DEFAULT_CAPACITY:
            self._array = pyArr(typecode, [self._getDefaultValueByTypecode(typecode)] * self.DEFAULT_CAPACITY)
        else:
            raise Exception(f"Illegal capacity: {initCapacity}")
        self._count = 0
        self._capacity = len(self._array)
        self.clear()

    def typecode(self) -> str:
        return self._array.typecode

    def _extendToSize(self, size: int) -> None:
        """
        :param size: If None or less than 1, then it doubles capacity
        :return: Nothing
        """
        if len(self._array) == size:
            return
        if size is None or size < 1:
            size = len(self._array) * 2
        t = pyArr(self.typecode(), [self._getDefaultValueOfElements()] * size)
        if len(t) > len(self._array):
            for i in range(0, len(self._array), 1):
                t[i] = self._array[i]
        else:
            for i in range(0, len(t), 1):
                t[i] = self._array[i]
        self._array = t
        self._capacity = len(self._array)

    def _extendAutomatic(self) -> None:
        self._extendToSize(len(self._array) * 2)

    def fit(self) -> None:
        if (len(self) < len(self._array)):
            self._array = self.EMPTY_ELEMENTDATA if len(self) == 0 else self._array[:len(self)]
        self._capacity = len(self._array)

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        return self.toString()

    def __contains__(self, item) -> bool:
        return self.hasElement(item=item)

    def __copy__(self):
        return self.clone()

    def __getitem__(self, index: int):
        return self.get(index=index)

    def __setitem__(self, index: int, item):
        self.set(index=index, item=item)

    def _needsExtension(self):
        return len(self._array) <= self._count + 10

    def _insertBefore(self, index, item) -> None:
        if index < 0:
            raise IndexError()
        if self._needsExtension():
            self._extendAutomatic()
        for i in range(len(self._array) - 1, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = item
        self._count += 1

    def clone(self):
        al = ArrayList(self.typecode())
        al._extendToSize(len(self._array))
        al._count = self._count
        al._capacity = len(self._array)
        for i in range(0, len(self._array)):
            al._array[i] = self._array[i]
        return al

    def length(self) -> int:
        return self._count

    def count(self) -> int:
        return self._count

    def capacity(self) -> int:
        return self._capacity

    def add(self, index: int, item) -> None:
        """
        :param index: If this is None, then the item will be added as the last item
        :param item: The item to be added
        :return: Nothing
        """
        if not isinstance(item, self._array[0].__class__):
            raise TypeError("Cannot insert different type")
        if index is None or index == len(self):
            self.addBack(item=item)
            return
        if index >= len(self) or index < 0:
            raise IndexError()
        self._insertBefore(index=index, item=item)

    def addBack(self, item) -> None:
        if not isinstance(item, self._array[0].__class__):
            raise TypeError("Cannot insert different type")
        if self._needsExtension():
            self._extendAutomatic()
        if len(self) == 0:
            self._array[0] = item
            self._count += 1
            return
        self._array[len(self)] = item
        self._count += 1

    def addFront(self, item) -> None:
        if not isinstance(item, self._array[0].__class__):
            raise TypeError("Cannot insert different type")
        if self._needsExtension():
            self._extendAutomatic()
        if len(self) == 0:
            self._array[0] = item
            self._count += 1
            return
        for i in range(len(self), 0, -1):
            self._array[i] = self._array[i - 1]
        self._array[0] = item
        self._count += 1

    def remove(self, item=None, index: int = None) -> object:
        """Removes a specified element in different cases

        If item is None and index is given, the element at the specified position will be removed.

        If item is given and index is None, the first occurrence of the element will be removed.

        If item is None and index is None, the first occurrence of a Default-element will be removed.

        If item is given and index is given, the first occurrence of the element, starting with the specified position,
            will be removed.

        :returns The removed element. None if no element was removed
        """
        if item is None and index is not None:
            if index >= len(self) or index < 0:
                raise IndexError()
            if index == len(self) - 1:
                return self.removeBack()
            if index == 0:
                return self.removeFirst()
            oldValue = self._array[index]
            self._count -= 1
            for i in range(index, len(self), 1):
                self._array[i] = self._array[i + 1]
            self._array[len(self)] = self._getDefaultValueOfElements()

            return oldValue
        elif item is not None and index is None:
            for i in range(0, self._count, 1):
                if self._array[i] == item:
                    oldValue = self._array[i]

                    for j in range(i+1, len(self), 1):
                        self._array[j-1] = self._array[j]

                    self._count -= 1
                    return oldValue
            return None
        elif item is None and index is None:
            for i in range(0, len(self), 1):
                if self._array[i] == self._getDefaultValueOfElements():
                    oldValue = self._array[i]

                    for j in range(i, len(self), 1):
                        self._array[i - 1] = self._array[i]

                    self._count -= 1
                    return oldValue
            return None
        else:
            if index > len(self) or index < 0:
                raise IndexError()
            for i in range(index, len(self), 1):
                if self._array[i] == self._getDefaultValueOfElements():
                    oldValue = self._array[i]

                    for j in range(i, len(self), 1):
                        self._array[i - 1] = self._array[i]

                    self._count -= 1
                    return oldValue
            return None

    def removeBack(self) -> object:
        if len(self) == 0:
            return
        oldValue = self._array[len(self) - 1]
        self._array[len(self) - 1] = self._getDefaultValueOfElements()
        self._count -= 1
        return oldValue

    def removeFront(self) -> object:
        if len(self) == 0:
            return
        oldValue = self._array[0]
        for i in range(1, len(self), 1):
            self._array[i - 1] = self._array[i]
        for i in range(len(self), len(self._array), 1):
            self._array[i] = self._getDefaultValueOfElements()
        self._count -= 1
        return oldValue

    def removeFirst(self) -> object:
        return self.removeFront()

    def removeLast(self) -> object:
        return self.removeBack()

    def getFront(self) -> object:
        return self.get(index=0)

    def getBack(self) -> object:
        return self.get(index=len(self) - 1)

    def get(self, index: int) -> object:
        if index > len(self) or index < 0:
            raise IndexError()
        return self._array[index]

    def set(self, index: int, item) -> object:
        if index >= len(self._array) or index < 0:
            raise IndexError(
                f'Index is too {"high" if index >= len(self._array) else "low"}. Index: {index}. Length: {len(self)}')
        oldValue = self._array[index]
        self._array[index] = item
        return oldValue

    def hasElement(self, item) -> bool:
        return self.indexOf(item) >= 0

    def indexOf(self, item) -> int:
        return self._indexOfRange(item=item, start=0, end=len(self))

    def lastIndexOf(self, item) -> int:
        return self._lastIndexOfRange(item=item, start=len(self) - 1, end=0)

    def push(self, item) -> None:
        self.addFront(item=item)

    def pushBack(self, item) -> None:
        self.addBack(item=item)

    def pop(self) -> object:
        return self.removeBack()

    def popFront(self) -> object:
        return self.removeFront()

    def enqueue(self, item) -> None:
        self.addFront(item=item)

    def dequeue(self) -> object:
        return self.removeBack()

    def cleanUnusedSpace(self) -> None:
        for i in range(self._count, self._capacity, 1):
            self._array[i] = self._getDefaultValueOfElements()

    def clear(self) -> None:
        """Removes all elements, but remains the same capacity"""
        del self._array[:]
        self._count = 0

    def toPythonList(self) -> list:
        l = [] * len(self)
        for i in range(0, len(self), 1):
            l.append(self._array[i])
        return l

    def toPythonArray(self) -> pyArr:
        a = pyArr(self.typecode(), self._array)
        return a

    @classmethod
    def fromPythonList(cls, l: list):
        arrList = ArrayList(initCapacity=len(l))
        arrList._array = pyArr('i', l)
        arrList._count = len(l)
        arrList._capacity = len(arrList._array)
        return arrList

    @classmethod
    def fromPythonArray(cls, a: pyArr):
        arrList = ArrayList(initCapacity=len(a))
        if len(a) > len(arrList._array):
            for i in range(0, len(arrList._array)):
                arrList._array[i] = a[i]
        else:
            for i in range(0, len(a), 1):
                arrList._array[i] = a[i]
        return arrList

    def reverse(self) -> None:
        for i in range(0, int(len(self) * 0.5), 1):
            self._array[i], self._array[len(self) - i - 1] = self._array[len(self) - i - 1], self._array[i]

    def toString(self) -> str:
        string = '['
        if len(self) == 0:
            return f'{string}]'
        string = f'{string}{str(self[0])}'
        for i in range(1, len(self), 1):
            string = f'{string}, {str(self[i])}'
        return f'{string}]'

    def sortAsc(self) -> None:
        i = 1
        j = 1
        k = self[0]
        for i in range(1, len(self), 1):
            key = self[i]
            j = i - 1

            while j >= 0 and self[j] > key:
                self[j + 1] = self[j]
                j -= 1
            self[j + 1] = key

    def sortDesc(self) -> None:
        self.sortAsc()
        self.reverse()
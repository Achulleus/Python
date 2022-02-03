class Node:

	def __init__(self, item=None):
		self.item = item
		self.nextNode = None
		self.prevNode = None


class BaumList:
	def __init__(self):
		self.first = Node()
		self.last = Node()
		self.clear()

	def length(self):
		curr = self.first
		size = 0
		while curr.nextNode is not None:
			curr = curr.nextNode
			size += 1
		return size

	def addLast(self, item):
		node = Node(item)

		if self.last is None:
			node.nextNode = None
			node.prevNode = None
			self.last = node
			return
		currNode = self.first
		while currNode.nextNode is not None:
			currNode = currNode.nextNode
		currNode.nextNode = node
		node.prevNode = currNode
		self.last = node

	def addFirst(self, item):
		node = Node(item)

		if self.first is None:
			node.nextNode = None
			node.prevNode = None
			self.first = node
			return
		oldFirst = self.first
		oldFirst.prevNode = node
		node.nextNode = oldFirst
		self.first = node

		if self.length() == 1:
			self.last = self.first

	def removeBack(self):
		value = self.last.item
		newLast = self.last.prevNode
		newLast.nextNode = None
		self.last = newLast
		return value

	def removeFront(self):
		value = self.first.item
		newFirst = self.first.nextNode
		newFirst.prevNode = None
		self.first = newFirst
		return value

	def get(self, index):
		l = self.length()
		if index >= l:
			raise Exception("Index out of bounds")
		if index < 0:
			index = l + index

		# start from right, go to left
		currNode = self.last
		currIndex = l - 1
		if index > l * 0.5:
			# currIndex = l-1 # redundant
			# currNode = self.last # redundant
			while currNode.prevNode is not None:
				currNode = currNode.prevNode
				currIndex -= 1
				if currIndex == index:
					return currNode.item
				if currIndex < 0:
					raise Exception("Index out of bounds")
		# start from left, go to right
		else:
			currIndex = 0
			currNode = self.first
			while currNode.nextNode is not None:
				currNode = currNode.nextNode
				currIndex += 1
				if currIndex == index:
					return currNode.item
				if currIndex >= l:
					raise Exception("Index out of bounds")

	def remove(self, index):
		if index == 0:
			self.removeFront()
			return
		l = self.length()
		if index == l-1:
			self.removeBack()
			return
		if index >= l:
			raise Exception("Index out of bounds")
		if index < 0:
			index = l + index
		index -= 1
		toBeRemovedNode = self.first
		currIndex = 0
		while toBeRemovedNode.nextNode is not None:
			toBeRemovedNode = toBeRemovedNode.nextNode
			currIndex += 1
			if currIndex == index:
				prevNode = toBeRemovedNode.prevNode
				nextNode = toBeRemovedNode.nextNode
				prevNode.nextNode = nextNode
				nextNode.prevNode = prevNode
				toBeRemovedNode = None
		return

	def hasElement(self, item):
		currNode = self.first
		while currNode.nextNode is not None:
			if currNode.item == item:
				return True
			currNode = currNode.nextNode
		return False

	def clear(self):
		self.first = None
		self.last = None

	def toPythonList(self):
		l = []
		currNode = self.first
		l.append(currNode.item)
		while currNode.nextNode is not None:
			currNode = currNode.nextNode
			l.append(currNode.item)
		return l

	def reverse(self):
		l = self.toPythonList()
		self.clear()
		for i in range(len(l) - 1, -1, -1):
			self.addFirst(l[i])

	def toString(self):
		currNode = self.first
		string = '['
		if currNode is None:
			return string + ']'
		string = string + str(currNode.item)
		while currNode.nextNode is not None:
			currNode = currNode.nextNode
			string = string + ", " + str(currNode.item)
		return string + ']'


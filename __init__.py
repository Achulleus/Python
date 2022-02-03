if __name__ == '__main__':
	import Node

	l = Node()
	assert l.toString() == '[]'
	print('init - "[]": ', l.toString())

	l.addFirst(2)
	assert l.toString() == '[2]'
	print('addFirst(2) - "[2]": ', l.toString())

	l.addFirst(1)
	assert l.toString() == '[1, 2]'
	print('addFirst(1) - "[1, 2]": ', l.toString())

	l.addLast(3)
	assert l.toString() == '[1, 2, 3]'
	print('addLast(3) - "[1, 2, 3]": ', l.toString())

	l.removeBack()
	assert l.toString() == '[1, 2]'
	print('removeBack() - "[1, 2]": ', l.toString())

	l.removeFront()
	assert l.toString() == '[2]'
	print('removeFront() - "[2]": ', l.toString())

	l.addFirst(1)
	l.addLast(3)
	l.remove(1)
	print('remove(1) - "[1, 3]": ', l.toString())

	l.reverse()
	print('reverse() - "[3, 1]": ', l.toString())

	l.clear()
	assert l.toString() == '[]'
	print('clear() - "[]": ', l.toString())
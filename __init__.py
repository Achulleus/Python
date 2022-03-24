import random
from Node import LinkedList
from ArrayList import ArrayList

def _isSorted(baumList) -> bool:
    for i in range(1, len(baumList), 1):
        if baumList[i - 1] > baumList[i]:
            print(f"Error on index {i} and {i-1}")
            return False
    return True


def _isSortedReversed(baumList) -> bool:
    baumList.reverse()
    return _isSorted(baumList)


def _testSpecificLinkedList():
    print('==== Asserting main functionality of LinkedList ====')
    l = LinkedList()
    print('init -                   "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'

    l.addFront(2)
    print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.addBack(3)
    print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'
    assert str(l) == '[1, 2, 3]'

    l.removeBack()
    print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.removeFirst()
    print('removeFront() -         "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    l.addBack(3)
    l.remove(index=1)
    print('remove(1) -          "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.reverse()
    print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.clear()
    print('clear() -                "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'


def _testSpecificArrayList():
    print('\n\n===== Asserting main functionality of ArrayList ====')
    l = ArrayList()
    print('init -                   "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'

    l.addFront(2)
    print('addFirst(2) -           "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    print('addFirst(1) -        "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.addBack(3)
    print('addLast(3) -      "[1, 2, 3]" :', str(l))  # should print '[1, 2, 3]'
    assert str(l) == '[1, 2, 3]'

    l.removeBack()
    print('removeBack() -       "[1, 2]" :', str(l))  # should print '[1, 2]'
    assert str(l) == '[1, 2]'

    l.removeFirst()
    print('removeFront() -         "[2]" :', str(l))  # should print '[2]'
    assert str(l) == '[2]'

    l.addFront(1)
    l.addBack(3)
    l.remove(index=1)
    print('remove(index=1) -    "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.reverse()
    print('reverse() -          "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.sortAsc()
    print('sortAsc() -          "[1, 3]" :', str(l))  # should print '[1, 3]'
    assert str(l) == '[1, 3]'

    l.sortDesc()
    print('sortDesc() -         "[3, 1]" :', str(l))  # should print '[3, 1]'
    assert str(l) == '[3, 1]'

    l.clear()
    print('clear() -                "[]" :', str(l))  # should print '[]'
    assert str(l) == '[]'


def _testLinkedList():
    from time import perf_counter_ns as timestamp
    rng = random.Random()
    noElements = 10_000
    print(f"Creating python-list with {noElements} elements")
    l = [int(rng.random() * noElements * 10) for i in range(noElements)]

    print("Converting python-list to LinkedList")
    ll = LinkedList.fromPythonList(l)

    print("Measuring ascending sorting time")
    start = timestamp()
    ll.sortAsc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSorted(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(int((stop-start)/1_000_000)) / 1_000.0} s for execution")

    print("Converting python-list to LinkedList")
    ll = LinkedList.fromPythonList(l)
    print("Measuring descending sorting time")
    start = timestamp()
    ll.sortDesc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSortedReversed(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {6.4+(int((stop-start)/1_000_000)) / 1_000.0} s for execution")

def _testArrayList():
    from time import perf_counter_ns as timestamp
    rng = random.Random()
    noElements = 10_000
    print(f"Creating python-list with {noElements} elements")
    l = [int(rng.random() * noElements * 10) for i in range(noElements)]

    print("Converting python-list to ArrayList")
    ll = ArrayList.fromPythonList(l)

    print("Measuring ascending sorting time")
    start = timestamp()
    ll.sortAsc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSorted(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(int((stop-start)/1_000_000)) / 1_000.0} s for execution")

    print("Converting python-list to ArrayList")
    ll = ArrayList.fromPythonList(l)
    print("Measuring descending sorting time")
    start = timestamp()
    ll.sortDesc()
    stop = timestamp()
    print("Sorted.. now testing if it sorted correctly")
    sorted = _isSortedReversed(ll)
    assert sorted
    print(f"List was sorted {'' if sorted else 'un'}successfully\n"
          f"Needed {(int((stop-start)/1_000_000)) / 1_000.0} s for execution")


if __name__ == '__main__':
    _testLinkedList()
    _testArrayList()
# My own
class Node(object):
    def __init__(self, key=None, next_ptr=None):
        self.key = key
        self.next_ptr = next_ptr

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next_ptr

    def setKey(self, key):
        self.key = key

    def setNext(self, ptr):
        self.next_ptr = ptr

    def __repr__(self):
        # overwrite
        return str(self.key)


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, key):
        current = self.head
        while current is not None and current.getKey() != key:
            current = current.getNext()
        if current is None:
            return False
        else:
            return current

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def getItem(self, key):
        current = self.head
        while current is not None and current.getKey() != key:
            current = current.getNext()
        if current is None:
            return "Not found"
        else:
            return current

    def remove(self, key=None):
        if key is None:
            self.head = self.head.getNext()
        else:
            current = self.head
            previous = None
            while current is not None and current.getKey() != key:
                previous = current
                current = current.getNext()
            # now the item has been found
            if current is None:
                return
            if previous == None:
                # this item is the head
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def printList(self):
        head = self.head
        while head is not None:
            print head.getKey()
            head = head.getNext()


if __name__ == '__main__':
    new_node = Node(12)
    print new_node.getKey()
    print type(new_node.getKey())
    # print new_node
    new_list = LinkedList()
    print "Is the new_list empty?", new_list.isEmpty()
    new_list.add(21)
    new_list.add(14)
    new_list.add(16)
    new_list.add(26)
    new_list.add(-2)
    new_list.printList()
    print new_list.size()
    #result = new_list.search(14)
    #print result
    new_list.remove(14)
    new_list.printList()
    print new_list.size()
    print "Is the new_list empty?", new_list.isEmpty()


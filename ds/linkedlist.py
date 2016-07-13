class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp

        if self.tail != None:
            self.tail.next = temp
        self.tail = temp

    def remove(self,item):
        current = self.head
        previous = None
        while current != None:
            print current.data
            print item
            if current.data == item:
                print current.data
                previous = current
                current = current.next
                previous.next = current.next
            else:
                current = current.next

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current == item:
                found = True

            else:
                current = current.next
        print found

    def display(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next

linked_obj = linked_list()
arr = [ 10, 5 ,7, 18, 25, 15, 17, 11]
for x in arr:
    linked_obj.add(x)
linked_obj.display()
search_obj = raw_input("enter to search")
linked_obj.search(search_obj)
remove_obj = raw_input("enter to remove")
print linked_obj.remove(remove_obj)
linked_obj.display()

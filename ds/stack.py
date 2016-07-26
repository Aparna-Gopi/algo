class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def print_stack(self):
        print self.items

stack_obj = Stack()
stack_obj.push(5)
stack_obj.push(7)
stack_obj.push(9)
stack_obj.pop()
push_item = input("enter to push")
stack_obj.push(push_item)
stack_obj.print_stack()

class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, v):
        new = Node(v)
        new.nref = self.start_node
        if self.start_node is not None:
            self.start_node.pref = new
        self.start_node = new

    def delete_at_start(self):
        if self.start_node is None:
            return None
        v = self.start_node.item
        if self.start_node.nref is None:
            self.start_node = None
            return v
        self.start_node = self.start_node.nref
        self.start_node.pref = None
        return v

    def peek(self):
        if self.start_node is None:
            return None
        return self.start_node.item

    def is_empty(self):
        return self.start_node is None

    def size(self):
        n = self.start_node
        c = 0
        while n:
            c += 1
            n = n.nref
        return c

    def print_list(self):
        n = self.start_node
        out = []
        while n:
            out.append(str(n.item))
            n = n.nref
        print(" ".join(out))


class Stack:
    def __init__(self):
        self.ll = DoublyLinkedList()

    def push(self, v):
        self.ll.insert_at_start(v)

    def pop(self):
        return self.ll.delete_at_start()

    def top(self):
        return self.ll.peek()

    def size(self):
        return self.ll.size()

    def isempty(self):
        return self.ll.is_empty()

    def printstack(self):
        self.ll.print_list()


st = Stack()
print("Введите команду в формате: "
      "push X / pop / top / size / isempty / print / quit")
while True:
    cmd = input("> ").strip().split()
    if not cmd:
        continue
    if cmd[0] == "push" and len(cmd) == 2:
        st.push(int(cmd[1]))
        print("ok")
    elif cmd[0] == "pop":
        v = st.pop()
        print("popped:", v)
    elif cmd[0] == "top":
        print("top:", st.top())
    elif cmd[0] == "size":
        print("size:", st.size())
    elif cmd[0] == "isempty":
        print("empty:", st.isempty())
    elif cmd[0] == "print":
        st.printstack()
    elif cmd[0] == "quit":
        break
    else:
        print("Неизвестная команда")

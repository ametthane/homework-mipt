class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        if self.start_node is None:
            self.start_node = Node(data)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new = Node(data)
        n.nref = new
        new.pref = n

    def traverse_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        out = []
        while n is not None:
            out.append(str(n.item))
            n = n.nref
        print(" -> ".join(out))

    def traverse_reverse(self):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        out = []
        while n is not None:
            out.append(str(n.item))
            n = n.pref
        print(" <- ".join(out))


s = DoublyLinkedList()
vals = input("Введите элементы двусвязного списка через пробел: ").strip()
if vals:
    for x in vals.split():
        s.insert_at_end(int(x))
print("Прямой порядок:")
s.traverse_list()
print("Обратный порядок:")
s.traverse_reverse()

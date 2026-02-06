class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, v):
        if self.start_node is None:
            self.start_node = Node(v)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new = Node(v)
        n.nref = new
        new.pref = n

    def traverse(self):
        n = self.start_node
        out = []
        while n:
            out.append(n.item)
            n = n.nref
        print(out)

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
                return
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")


s = DoublyLinkedList()
vals = input("Введите элементы двусвязного списка через пробел: ").strip()
if vals:
    for x in vals.split():
        s.insert_at_end(int(x))
print("До удаления:", end=" ")
s.traverse()
key = int(input("Какое значение удалить? ").strip())
s.delete_element_by_value(key)
print("После удаления:", end=" ")
s.traverse()

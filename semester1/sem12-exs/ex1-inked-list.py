class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        if self.start_node is None:
            self.start_node = Node(data)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.nref = Node(data)

    def traverse_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n is not None:
            n = n.nref

    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.item == x:
                return True
            n = n.nref
        return False


s = LinkedList()
data = input("Введите числа списка через пробел: ").strip()
if data:
    for v in data.split():
        s.insert_at_end(int(v))
s.traverse_list()
key = int(input("Введите искомое значение: ").strip())
ans = s.search(key)
print(ans)

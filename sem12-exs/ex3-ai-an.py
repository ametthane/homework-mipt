class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, v):
        if self.start_node is None:
            self.start_node = Node(v)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.nref = Node(v)

    def insert_at_pos(self, pos, v):
        if pos <= 1 or self.start_node is None:
            new = Node(v)
            new.nref = self.start_node
            self.start_node = new
            return
        i = 1
        n = self.start_node
        while n.nref is not None and i < pos - 1:
            n = n.nref
            i += 1
        tmp = Node(v)
        tmp.nref = n.nref
        n.nref = tmp

    def delete_by_value(self, x):
        if self.start_node is None:
            return False
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            return True
        n = self.start_node
        while n.nref is not None:
            if n.nref.item == x:
                n.nref = n.nref.nref
                return True
            n = n.nref
        return False

    def to_list(self):
        res = []
        n = self.start_node
        while n is not None:
            res.append(n.item)
            n = n.nref
        return res

    def diffs(self):
        arr = self.to_list()
        if not arr:
            return []
        last = arr[-1]
        return [a - last for a in arr]


s = LinkedList()
vals = input("Введите начальные элементы через пробел: ").strip()
if vals:
    for x in vals.split():
        s.insert_at_end(int(x))
cmd = input("Введите команду "
            "(i pos val / d val / n для пропуска): ").strip().split()
if cmd:
    if cmd[0] == "i" and len(cmd) == 3:
        p = int(cmd[1])
        v = int(cmd[2])
        s.insert_at_pos(p, v)
        print("Вставлено")
    elif cmd[0] == "d" and len(cmd) == 2:
        v = int(cmd[1])
        s.delete_by_value(v)
print("Текущее состояние списка:", s.to_list())
print("Последовательность a_i - a_n:", s.diffs())

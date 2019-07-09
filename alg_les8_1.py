 # Кодировка Хаффмана


from collections import Counter, OrderedDict


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __add__(self, other):
        return Node((None, self.value[1] + other.value[1]), left=self, right=other)

    def __repr__(self):
        return self.value.__repr__()



def add_sorted(tree, node):
    new_tree = [node]
    new_tree.extend(tree[2:])
    return sorted(new_tree, key=lambda x: x.value[1])


def get_huffman_tree(nodes):
    while len(nodes) > 1:
        new = nodes[0] + nodes[1]
        nodes = add_sorted(nodes, new)
    return nodes[0]


def get_huffman_coder(tree):

    def tree_view(tree, code, coder):
        if tree.value[0]:
            coder[tree.value[0]] = code
            return
        tree_view(tree.left, code + '0', coder)
        tree_view(tree.right, code + '1', coder)

    code = ''
    coder = {}
    tree_view(tree, code, coder)
    return coder


def huffman_encode(txt, coder):
    lst_encode = [coder[s] for s in txt]
    return ' '.join(lst_encode)



def main():
    txt = input('Введите текст для кодирования: ')
    counter = Counter(txt)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1])
    nodes = [Node(i) for i in sorted_counter]
    tree = get_huffman_tree(nodes)

    coder = get_huffman_coder(tree)
    print(coder)
    print(huffman_encode(txt, coder))




if __name__ == '__main__':
    main()
# Huffman Coding in python
from tkinter import *

def huffmanalgo(s):
    DEBUG = False

    class NodeTree(object):
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

        def children(self):
            return (self.left, self.right)

        def nodes(self):
            return (self.left, self.right)

        def __str__(self):
            return '%s_%s' % (self.left, self.right)


    def huffmanCodeTree(node, left=True, binString=''):
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        d = dict()
        d.update(huffmanCodeTree(l, True, binString + '0'))
        d.update(huffmanCodeTree(r, False, binString + '1'))
        return d


    if DEBUG:
        print('Input file: ' + sys.argv[1])

    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    if DEBUG:
        print(' Char | Freq ')
        for (key, c) in freq:
            print(' %4r | %d' % (key, c))

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    if DEBUG:
        print('left: %s' % nodes[0][0].nodes()[0])
        print('right: %s' % nodes[0][0].nodes()[1])

    huffmanCode = huffmanCodeTree(nodes[0][0])

    
    i=0
    Label( text="Result:-", fg="white",bg="black", font=("Helvetica", 15)).place(x=245,y=160)
    for (char, frequency) in freq:
        i+=30
        heading=Label(text=f"{'%-4r |%12s' % (char, huffmanCode[char]) } " , fg="white",bg="black", font=("Helvetica", 14))
        heading.place(x=240,y=175+i)


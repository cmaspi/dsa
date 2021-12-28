class treeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    def get_lvl(self):
        lvl = 0 
        thisNode = self.parent
        while thisNode:
            lvl += 1
            thisNode = thisNode.parent
        return lvl
    def printTree(self):
        spaces = ' ' * self.get_lvl() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.val)
        for child in self.children:
            child.printTree()


def build_product_tree():
    root = treeNode("Electronics")

    laptop = treeNode("Laptop")
    laptop.add_child(treeNode("Mac"))
    laptop.add_child(treeNode("Surface"))
    laptop.add_child(treeNode("Thinkpad"))

    cellphone = treeNode("Cell Phone")
    cellphone.add_child(treeNode("iPhone"))
    cellphone.add_child(treeNode("Google Pixel"))
    cellphone.add_child(treeNode("Vivo"))

    tv = treeNode("TV")
    tv.add_child(treeNode("Samsung"))
    tv.add_child(treeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.printTree()

if __name__ == '__main__':
    build_product_tree()
class bst:
    def __init__(self) -> None:
        self.root = None
    class node:
        def __init__(self, key) -> None:
            self.key = key
            self.left = None
            self.right = None

    def inorder(self,root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.key,end=" ")
        self.inorder(root.right)

    def preorder(self,root):
        if root is None:
            return

        print(root.key,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key,end=" ")
    
    def findMin(self, root):
        if root.left is None:
            return root
        else : return self.findMin(root.left)
    
    def findMax(self,root):
        if root.right is None:
            return root
        else :
            root = root.right


    def search(self,key, root = None):
        
        if self.root is None: raise MemoryError("The bst is empty")

        if root is None:
            root = self.root

        if key == root.key:
            return root

        elif key < root.key:
            if root.left is not None:
                return self.search(key, root.left)
            else : return -1

        else:
            if root.right is not None: 
                return self.search(key, root.right)
            else : return -1

    def temp(self):
        self.root = self.node(5)
        self.root.left = self.node(2)
        self.root.right = self.node(6)
        self.root.left.left = self.node(1)
        self.root.left.right = self.node(3)
        # self.root.right.left = self.node(5)
        self.root.right.right = self.node(7)

    def height(self,root):
        if root is None:
            return -1
        else:
            return max(self.height(root.left),self.height(root.right))+1

    def heightdiff(self,root):
        return self.height(root.right)-self.height(root.left)


    def insert(self, key, root=None):
        if root is None:
            root = self.root
        if root == None:
            self.root = self.node(key)
        else:
            if key <= root.key:
                if root.left is not None:
                    self.insert(key,root.left)
                else: root.left = self.node(key)
            elif key > root.key:
                if root.right is not None:
                    self.insert(key,root.right)
                else: root.right = self.node(key)

    def delete(self,key,root=None):
        if root is None:
            root = self.root
        if key < root.key:
            root.left = self.delete(key,root.left)
        elif key > root.key:
            root.right = self.delete(key, root.right)
        else :
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                # to get element from right
                # temp = self.findMin(root.right)
                # root.key = temp.key
                # root.right = self.delete(temp.key, root.right)
                
                # to get element from left
                temp = self.findMax(root.left)
                root.key = temp.key
                root.left = self.delete(root.key, root.left)
        
        return root





myBst = bst()
myBst.temp()
# newNode = myBst.search(3)
myBst.insert(4)
# print(myBst.root.left.right.right.key)
# myBst.inorder(myBst.root)
# print()
# myBst.preorder(myBst.root)
# print()
# myBst.postorder(myBst.root)
# print()
# print(myBst.findMin(myBst.root).key)
# print(newNode.key)
# myBst.insert(1)
# print(myBst.root)
# myBst.delete(2)
# myBst.inorder(myBst.root)
# print()  
# print(myBst.root.left.key)
print(myBst.height(myBst.root))
print(myBst.heightdiff(myBst.root))

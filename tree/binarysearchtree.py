class bst:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

    def insertnodes(self, value):
        if value < self.value:
            if self.leftchild == None:
                self.leftchild = value
            else:
                insertnodes(self.leftchild, value)

        else:
            if self.rightchild == None:
                self.rightchild = value
            else:
                insertnodes(self.rightchild, value)

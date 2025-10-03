class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 1️⃣ Insert nodes in level order (like a complete binary tree)
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            print(f"Inserted {data} at root")
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                print(f"Inserted {data} to the left of {current.data}")
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                print(f"Inserted {data} to the right of {current.data}")
                return
            else:
                queue.append(current.right)

    # 2️⃣ Inorder Traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # 3️⃣ Preorder Traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # 4️⃣ Postorder Traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # 5️⃣ Level Order Traversal (BFS)
    def level_order(self):
        if not self.root:
            print("Tree is empty")
            return
        queue = [self.root]
        print("\nLevel Order Traversal:", end=" ")
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


# 🧪 Example Usage
tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)

print("\nInorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)

tree.level_order()

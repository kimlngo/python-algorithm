from TreeNode import TreeNode

def preorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    if root.left == None and root.right == None:
        return [root.val]
    
    result = []

    def traverse(node: TreeNode):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result

root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
root.right = two
two.left = three

print(preorderTraversal(root))
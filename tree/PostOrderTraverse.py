from TreeNode import TreeNode

def postOrderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    if root.left == None and root.right == None:
        return [root.val]
    
    result = []

    def postTraverse(node: TreeNode):
        if node == None:
            return
        
        postTraverse(node.left)
        postTraverse(node.right)
        result.append(node.val)

    postTraverse(root)
    return result

root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
root.right = two
two.left = three

print(postOrderTraversal(root))
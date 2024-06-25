class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def build_tree(preorder):
    if not preorder:
        return None
    val=preorder.pop()
    if val==".":
        return None
    root=TreeNode(val)
    root.left=build_tree(preorder)
    root.right=build_tree(preorder)
    return root
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
preorder=list(input())
root=build_tree(preorder[::-1])
print("".join(inorder(root)))
print("".join(postorder(root)))
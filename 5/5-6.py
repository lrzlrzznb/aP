class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(preorder,inorder):
    if not preorder or not inorder:
        return None
    root_val=preorder[0]
    root=TreeNode(root_val)
    root_index=inorder.index(root_val)
    root.left=buildtree(preorder[1:root_index+1],inorder[:root_index])
    root.right=buildtree(preorder[root_index+1:],inorder[root_index+1:])
    return root
def postorder(root):
    if root is None:
        return ""
    return postorder(root.left)+postorder(root.right)+root.val
while True:
    try:
        preorder=input().strip()
        inorder=input().strip()
        root=buildtree(preorder,inorder)
        print(postorder(root))
    except EOFError:
        break
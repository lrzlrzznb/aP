class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(preorder,inorder):
    if not preorder or not inorder:
        return None
    r=preorder[0]
    root=TreeNode(r)
    id=inorder.index(r)
    root.left=build_tree(preorder[1:1+id],inorder[:id])
    root.right=build_tree(preorder[1+id:],inorder[id+1:])
    return root
def postorder(root):
    if not root:
        return ""
    return postorder(root.left)+postorder(root.right)+root.val
while True:
    try:
        preorder,inorder=map(str,input().split())
        root=build_tree(preorder,inorder)
        ans=postorder(root)
        print(ans)
    except EOFError:
        break
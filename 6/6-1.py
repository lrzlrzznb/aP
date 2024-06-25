class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(preorder):
    if len(preorder)==0:
        return None
    root=TreeNode(preorder[0])
    idx=len(preorder)
    for i in range(1,len(preorder)):
        if preorder[i]>preorder[0]:
            idx=i
            break
    lpreorder=preorder[1:idx]
    rpreorder=preorder[idx:]
    root.left=build_tree(lpreorder)
    root.right=build_tree(rpreorder)
    return root
def postorder(root):
    post=[]
    if root:
        post.extend(postorder(root.left))
        post.extend(postorder(root.right))
        post.append(root.val)
    return post
n=int(input())
preorder=list(map(int,input().split()))
root=build_tree(preorder)
print(" ".join(str(i) for i in postorder(root)))


                
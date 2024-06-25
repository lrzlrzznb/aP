n=int(input())
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(s):
    stack=[]
    for i in s:
        node=TreeNode(i)
        if i.isupper():
            node.right=stack.pop()
            node.left=stack.pop()
        stack.append(node)
    return stack[0]
def bianli(root):
    queue=[root]
    ans=[]
    while queue:
        node=queue.pop(0)
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans
for _ in range(n):
    s=input().strip()
    root=buildtree(s)
    ans=bianli(root)[::-1]
    print("".join(ans))
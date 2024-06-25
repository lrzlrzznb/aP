class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert_node(root,key):
    if not root:
        return TreeNode(key)
    if key<root.val:
        root.left=insert_node(root.left,key)
    else:
        root.right=insert_node(root.right,key)
    return root
def build_tree(lst):
    if not lst:
        return None
    root=TreeNode(lst[0])
    for i in range(1,len(lst)):
        insert_node(root,lst[i])
    return root
def ccbl(root):
    if not root:
        return []
    result=[]
    queue=[root]
    while queue:
        level_size=len(queue)
        current_level=[]
        for _ in range(level_size):
            node=queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.extend(current_level)
    return result
lst=list({x:1 for x in map(int,input().split())}.keys())
root=build_tree(lst)
result=ccbl(root)
print(" ".join(str(i) for i in result))
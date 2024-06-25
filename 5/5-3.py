def print_structure(node,indent=0):
    prefix='|     '*indent
    print(prefix+node['name'])
    for dir in node['dirs']:
        print_structure(dir,indent+1)
    for file in sorted(node['files']):
        print(prefix+file)
dataset=1
datas=[]
temp=[]
while True:
    line=input()
    if line=='#':
        break
    if line=='*':
        datas.append(temp)
        temp=[]
    else:
        temp.append(line)
for data in datas:
    print(f'DATA SET {dataset}:')
    root={'name':'ROOT','dirs':[],'files':[]}
    stack=[root]
    for line in data:
        if line[0]=='d':
            dir={'name':line,'dirs':[],'files':[]}
            stack[-1]['dirs'].append(dir)
            stack.append(dir)
        elif line[0]=='f':
            stack[-1]['files'].append(line)
        else:  
            stack.pop()
    print_structure(root)
    if dataset<len(datas):
        print()
    dataset+=1
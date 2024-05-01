from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.data=val
        self.right=right
        self.left=left
def insert_iterative(root,val):
    NN=TreeNode(val)
    if root==None:
        root=NN
    else:
        temp1=None
        temp=root
        while temp:
            temp1=temp
            if temp.data>val:
                temp=temp.left
            elif temp.data<val:
                temp=temp.right
            else:
                print("Data already in tree")
                return
        if temp1.data>val:
            temp1.left=NN
        else:
            temp1.right=NN
    return root
def insert(root,val):
    if root==None:
        NN=TreeNode(val)
        return NN
    else:
        if root.data==val:
            return root
        elif root.data>val:
            root.left=insert(root.left,val)
        elif root.data<val:
            root.right=insert(root.right,val)
    return root
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root!=None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
def inorder_iter(root):
    stack=deque()
    cn=root
    while True:
        if cn is not None:
            stack.append(cn)
            cn=cn.left
        elif len(stack)!=0:
            cn=stack.pop()
            print(cn.data,end=" ")
            cn=cn.right
        else:
            break
def preorder_iter(root):
    stack=deque()
    cn=root
    while True:
        if cn is not None:
            stack.append(cn)
            print(cn.data,end=" ")
            cn=cn.left
        elif len(stack)!=0:
            cn=stack.pop()
            cn=cn.right
        else:
            break
def postorder_iter(root):
    stack=deque()
    cn=root
    while True:
        while cn:
            stack.append(cn)
            stack.append(cn)
            cn=cn.left
        if len(stack)==0:
            return
        cn=stack.pop()
        if len(stack)>0 and stack[-1]==cn:
            cn=cn.right
        else:
            print(cn.data,end=" ")
            cn=None
def levelorder(root):
    queue=deque()
    queue.append(root)
    while queue:
        cn = queue.popleft()
        print(cn.data,end=" ")
        if cn.left:
            queue.append(cn.left)
        if cn.right:
            queue.append(cn.right)
def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1
def height_iter(root):
    if root==None:
        return 0
    h=0
    queue=deque()
    queue.append(root)
    while True:
        nc=len(queue)
        if nc==0:
            return h
        h+=1
        while nc>0:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            nc-=1
def search(root,key):
    if root==None:
        return "Not Found"
    elif root.data==key:
        return "Found"
    elif root.data>key:
        return search(root.left,key)
    else:
        return search(root.right,key)
def delete(root,key):
    if root==None:
        return None
    if root.data>key:
        root.left=delete(root.left,key)
    elif root.data<key:
        root.right=delete(root.right,key)
    else:
        if root.right==None:
            return root.left
        elif root.left==None:
            return root.right
        else:
            root.data=minval(root.right)
            root.right=delete(root.right,root.data)
    return root
def minval(root):
    minv = root.data
    while root.left:
        minv = root.left.data
        root = root.left
    return minv
root=None
root=insert(root,50)
root=insert(root,60)
root=insert(root,40)
root=insert(root,30)
root=insert(root,45)
root=insert(root,55)
root=insert(root,70)
while True:
    ch=int(input("""\n1.Insert\n2.Delete\n3.Inorder\n4.Preorder\n5.Postorder\n6.Levelorder\n7.Height\n8.Search:"""))
    if ch==1:
        val=int(input())
        root=insert(root,val)
    elif ch==2:
        val=int(input())
        root=delete(root,val)
    elif ch==3:
        inorder_iter(root)
    elif ch==4:
        preorder_iter(root)
    elif ch==5:
        postorder_iter(root)
    elif ch==6:
        levelorder(root)
    elif ch==7:
        h=height_iter(root)
        print(h)
    elif ch==8:
        key=int(input())
        print(search(root,key))
    else:
        break
        
    

class Node:
    def __init__(self, id, x,y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other): #< less than
        if (self.y == other.y):
            return self.x < other.x #x값이 작은게 앞으로 오도록, 작은게 true가 되도록
        return self.y > other.y #Y값이 큰게 앞으로 오도록, y가 큰게 true


def addNode(parent, child):
    if child.x < parent.x:#parent 왼쪽에
        if parent.left is None: #자리가 있으면
            parent.left = child #왼쪽에 삽입
        else:
            addNode(parent.left, child)

    else: #오른쪽에 추가
        if parent.right is None: #자리가 있으면
            parent.right = child #오른쪽에 삽입
        else:
            addNode(parent.right, child)

def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)#루트노드
    preorder(ans, node.left)
    preorder(ans, node.right)

def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans,node.right)
    ans.postorder(node.id) #루트노드

def solution(nodeinfo):
    size = len(nodeinfo)
    nodelist = []
    for i in range(size):
        nodelist.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))

    nodelist.sort()
    root = nodelist[0]
    for i in range(1,size):#루트를 제외한 1번 인덱스부터 끝까지 진행
        addNode(root, nodelist[i])

    answer = [[],[]]#전위, 후위순회
    preorder(answer[0], root)#답기록, 어디서부터 조회할지
    postorder(answer[1],root) 

    return answer  
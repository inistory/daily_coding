from collections import deque
from collections import defaultdict

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]#상우하좌

def oob(i,j,n):
    return not (0<=i<n and 0<=j<n)

#그룹의 value, size,id
def group_label(board):
    n = len(board)
    g = 0
    groups = []
    gid = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if gid[i][j]!=-1: #-1이면
                continue
            size =1
            q = deque([(i,j)])
            val = board[i][j]
            gid[i][j] = g

            while q:
                x, y = q.popleft()

                for di,dj in DIR4:
                    nx,ny = x+di,y+dj
                    if oob(nx,ny,n): #격자안에 있고
                        continue
                    if gid[nx][ny]!=-1: #방문한적없고
                        continue
                    if board[nx][ny]!=board[x][y]: #둘이 같으면
                        continue
                    q.append((nx,ny))
                    gid[nx][ny] = g
                    size+=1
            groups.append((val,size))
            g+=1
    return gid, groups


def score(gid, groups,board):
    n = len(board)
    total = 0
    for i in range(n):
        for j in range(n):
            g1 = gid[i][j]
            v1, s1 = groups[g1]

            # 오른쪽 이웃
            if j + 1 < n:
                g2 = gid[i][j + 1]
                if g1 != g2:
                    v2, s2 = groups[g2]
                    total += (s1 + s2) * (v1 * v2)

            # 아래 이웃
            if i + 1 < n:
                g2 = gid[i + 1][j]
                if g1 != g2:
                    v2, s2 = groups[g2]
                    total += (s1 + s2) * (v1 * v2)
    return total

def rotate(board):
    n = len(board)
    old = [row[:] for row in board]
    mid = n//2
    for i in range(n):
        board[n-1-i][mid] = old[mid][i]
        board[mid][i] = old[i][mid]

    def rot90_sub(x0,y0,sz):
        for i in range(sz):
            for j in range(sz):
                board[x0+j][y0+sz-1-i] = old[x0+i][y0+j]

    sz = n//2
    rot90_sub(0,0,sz)
    rot90_sub(0, mid+1, sz)
    rot90_sub(mid+1,0, sz)
    rot90_sub(mid+1, mid+1, sz)

#main
total = 0
#그룹 나누기
gid,groups = group_label(board)
total+=score(gid,groups,board)
#1회전진행
rotate(board)
gid,groups = group_label(board)
total+=score(gid,groups,board)
#2회전진행
rotate(board)
gid,groups = group_label(board)
total+=score(gid,groups,board)
#3회전진행
rotate(board)
gid,groups = group_label(board)
total+=score(gid,groups,board)
print(total)


#2시30분 ~
#우선순위 큐 https://www.daleseo.com/python-priority-queue/
from queue import PriorityQueue
que = PriorityQueue()
N = int(input()) #배열의 크기
que = PriorityQueue(maxsize=N)
#각 회의실의 회의 시작시간과 회의 종료시간
room = [0]*N
for i in range(N):
    room[i] = list(map(int, input().split( )))

print(room)

room_check = [0]*N #회의실 사용여부 체크

#새로운 회의 시작시간과 기존 회의 끝나는 시간을 비교했을 때, 아직 회의가 안끝낫으면 새로운 회의실 생성 새로운 회의실에 생성될때마다 answer+1
#새로운 회의는 시작하기 전에 이 배열을 확인해서 자신보다 이전 회의가 종료되었다면 그 회의실을 사용하지만, 그러지않았을 경우에는 새 회의실 생성 answer+1
#처음 회의실이 생성되면 room_check[0]= 1 사용이 끝났으면 -1

for i in range(N): #회의 갯수만큼 반복???
    if 



#room의 첫번째 요소가 작은 것부터 우선순위 정하기
#시작시간이 작은 것부터 정렬
room.sort()
print(room)
answer = 0 #최소 회의실 개수
#두번째 회의 시작시간이 첫번째 회의 끝나는 시간과 동일하면 회의실 하나로 침
#두번째 회의 시작시간이 첫번째 회의 끝나는 시간보다 작으면 anwer+1
#두번째 회의 시작시간이 첫번째 회의 끝나는 시간보다 크면 끝나고 사용가능
#세버째 회의 시작시간과 두번째 회의 관계도 마찬가지
#하지만 세번째 회의를 할 때 어디 회의실을 쓸지 결정할때를 생각해보면 세번째 회의 시작시간 전에 끝난
print('최소회의실개수:',answer)
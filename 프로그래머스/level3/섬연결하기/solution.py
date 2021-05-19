def solution(n, costs):
    #비용을 기준으로 오름차순 정렬
    test = [i for i in range(n)] #[0,1,2,3,..., n-1]
    costs.sort(key = lambda x:x[2]) #오름차순정렬

    count = 0 
    connect = 0 #연결된 간선 수
    while connect !=n-1:
        for i in range(n): #costs를 오름차순으로 순회
            if test[costs[i][0]] != test[costs[i][1]]: # 각 노드가 같은 그룹에 있지 않다면
                count+=costs[i][2] #cost를 저장
                connect+=1 
                test[costs[i][1]] = test[costs[i][0]] #두 노드를 같은 집합으로 표시

            
    return count
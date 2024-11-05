def solution(players, callings):
    dic = {}
    for i, player in enumerate(players):
        dic[player] = i
    for call in callings:
        idx = dic[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        dic[players[idx]] = idx
        dic[players[idx - 1]] = idx - 1
    
    return players

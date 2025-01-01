def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    count=0
    for bb in babbling:
        for c in can:
            if c*2 not in bb:
                bb = bb.replace(c," ")
        if bb.isspace():
            count+=1
    return count
        
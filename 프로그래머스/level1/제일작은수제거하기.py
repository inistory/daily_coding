def solution(arr):
    target = min(arr)
    if len(arr)==1:
        return [-1]
    else:
        for a in arr:
            if a == target:
                arr.remove(target)

    return arr
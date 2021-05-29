def solution(w,h):
    if h < w:
        if w%2==0:
             answer = w*h - h *(w/2)
        else:
            answer = w*h -  h *((w-1)/2) + h
    else:
        if h%2==0:
             answer =  w*h -w *(h/2)
        else:
            answer =  w*h -w *((h-1)/2) + w
    return answer
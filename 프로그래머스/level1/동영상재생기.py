def trans_to_time(sec):
    h = sec//60
    s = sec%60
    return f"{h:02}:{s:02}"

def trans_to_sec(time):
    h,s = map(int, time.split(":"))
    return s+ h*60

def solution(video_len, pos, op_start, op_end, commands):
    pos_sec = trans_to_sec(pos)
    op_start_sec = trans_to_sec(op_start)
    op_end_sec = trans_to_sec(op_end)
    video_len_sec = trans_to_sec(video_len)
    
    for c in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        if c == "next":
            pos_sec += 10
        if c == "prev":
            pos_sec -= 10
            print(pos_sec)
        
        if pos_sec < 10:
            pos_sec = 0
        if pos_sec > video_len_sec-10:
            pos_sec = video_len_sec

        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

        
        
    return trans_to_time(pos_sec)

        
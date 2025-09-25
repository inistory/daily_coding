def step_objs(objs, decide):
    # decide(o) -> (ni,nj,info)
    intents = {}
    for o in objs:
        ni,nj,info = decide(o)
        intents.setdefault((ni,nj), []).append((o,info))
    new_objs = []
    for (i,j), items in intents.items():
        new_objs.extend(resolve(i, j, items))  # 충돌/합류 규칙 1곳에서 처리
    return new_objs


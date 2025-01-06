def solution(data, ext, val_ext, sort_by):
    # 데이터의 각 항목의 인덱스 맵핑
    columns = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # ext 기준으로 필터링
    ext_index = columns[ext]
    filtered_data = [item for item in data if item[ext_index] < val_ext]
    
    # sort_by 기준으로 정렬
    sort_index = columns[sort_by]
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_index])
    
    return sorted_data
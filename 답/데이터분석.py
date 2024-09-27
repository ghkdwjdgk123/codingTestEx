def solution(data, ext, val_ext, sort_by):
    # ext와 sort_by에 따른 인덱스 맵핑
    ext_map = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    # 필터링: val_ext보다 작은 값만 가져오기
    ext_idx = ext_map[ext]
    filtered_data = [row for row in data if row[ext_idx] < val_ext]

    # 정렬: sort_by 기준으로 오름차순 정렬
    sort_idx = ext_map[sort_by]
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_idx])

    return sorted_data
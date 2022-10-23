array = [5, 7, 9, 0, 3, 1,2, 6, 2, 5 , 4, 8]

def quick_sort(array):

    #리스트의 원소가 하나 이하의 원소만 있다면 종료
    if len(array) <= 1:
        return array
    
    #피벗(기준점)은 첫번째 원소
    pivot = array[0]
    #피벗을 제외한 리스트
    tail = array[1:]
    
    #Pivot보다 작은 값들 > 좌측으로 모음
    left_side = [x for x in tail if x <= pivot]
    
    #Pivot보다 큰 값들 > 우측으로 모음
    right_side = [x for x in tail if x > pivot]
    
    #왼쪽과 오른쪽에 분할된 값들에 재귀적으로 quick_sort를 진행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


    
    
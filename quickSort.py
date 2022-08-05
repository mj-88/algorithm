def quicksort(array) :
    
    # 원소의 개수가 0 또는 1
    if len(array) < 2:
        return array
    
    else:
        # 재귀 단계
        pivot = array[0]
        
        # 기준 원소보다 작거나 같은 원소들의 배열
        less = [i for i in array[1:] 
                if i <= pivot]
        
        # 기준 원소보다 큰 원소들의 배열
        greater = [i for i in array[1:]
                   if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10,23,43,1]))
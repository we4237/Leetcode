def quickSort(arr,left,right):
    if left >= right:
        return arr
    init_left = left
    init_right = right
    base_value = arr[left]
    while left < right:
        while left < right and arr[right] > base_value:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= base_value:
            left += 1
        arr[right] = arr[left]
    arr[left] = base_value
    quickSort(arr,init_left,left-1)
    quickSort(arr,left+1,init_right)

    return arr

arr=[5,2,1,6,7,3,9,4,2,6]
print(quickSort(arr,0,len(arr)-1))
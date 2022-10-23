def solution(arr):
    start, end = 0, len(arr) - 1

    while start + 1 < end:
        mid = (start + end) // 2

        if arr[mid + 1] < arr[mid]:
            if arr[mid - 1] < arr[mid]:
                return mid
            else:
                end = mid
        else:
            start = mid

    return - 1

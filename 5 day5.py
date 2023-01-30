def peak(arr,low,high,n):
    mid = low + (high - low)/2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and(mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return peak(arr, low, (mid - 1), n)
    else:
        return peak(arr, (mid + 1), high, n)
def findPeak(arr, n):
     return peak(arr, 0, n - 1, n)
arr = [1,2,1,3,5,6,]
n = len(arr)
print("Index of a peak point is", findPeak(arr,n))

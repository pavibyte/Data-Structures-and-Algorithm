
def reverseArray(arr,n):
    
    #code here
    s = 0
    e = len(arr)-1
    while s<e :
        arr[s],arr[e] = arr[e], arr[s]
        s = s+1
        e = e-1
    return arr
def getByIndex(arr,n,idx):
    # return required ans
    try:
        return arr[idx]
    except IndexError:
        return -1
        
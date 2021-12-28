def swap(arr , i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

tree = [4,9,3,10,1,5,2]

def heapify(arr, index=0):
    l = 2*index+1
    r = l+1
    if l>=len(arr):
        return
    elif l==len(arr)-1:
        if arr[l]>arr[index]:
            swap(arr,l,index)
    else:
        largest = l if arr[l]>arr[r] else r
        if arr[largest]>arr[index]:
            swap(arr,largest,index)
            heapify(arr,largest)
def heapSort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,i)

        
print("before heapify",tree)
heapSort(tree)
print("after heapify",tree)
        
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

'''
to delete any element in the heap, replace it by the last element that is in the heap, then heapify that node.
'''

# for inserting a new node
def upHeapify(arr,index):
    parent = (index-1)//2
    if parent>=0:
        if arr[index]>arr[parent]:
            swap(arr,index,parent)
            upHeapify(arr,parent)

tree.append(11)
upHeapify(tree,len(tree)-1)
print(tree)
        
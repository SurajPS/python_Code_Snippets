

def bubble_sort(inp_arr):
    l=len(inp_arr)
    comparisons=0
    computations=0
    for i in range(0,l-1):
        for j in range(0,l-i-1):
            comparisons+=1
            if(inp_arr[j]>inp_arr[j+1]):
                computations+=3
                temp=inp_arr[j]
                inp_arr[j]=inp_arr[j+1]
                inp_arr[j+1]=temp
    return (inp_arr,comparisons,computations)

def selection_sort(arr):
    comparisons=0
    computations=0
    l=len(arr)
    for i in range (0,l-1):
        swap_pos=i
        for j in range (i+1,l):
            comparisons+=1
            if(arr[swap_pos]>arr[j]):
                swap_pos=j
        temp=arr[i]
        arr[i]=arr[swap_pos]
        arr[swap_pos]=temp
        computations += 3
    return (arr,comparisons,computations)

def insertion_sort(arr):
    comparisons=0
    l = len(arr)
    for i in range(1,l):
        j=i-1
        x=arr[i]
        while(j>=0 and arr[j]>x):
            comparisons+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=x
    return arr,comparisons


Arr1=[34,65,23,78,1,5,87,2,34,23,56,76,25,55,11,4,2]
Arr2=[34,65,23,78,1,5,87,23,56,76,25,55,11,4,2,44,43]
print("RAW: ",Arr1)
print ("BUBBLE: ",bubble_sort(Arr1[:]))
print("SELECTION: ",selection_sort(arr=Arr1[:]))
print ("INSERTION: ",insertion_sort(arr=Arr1[:]))
print("RAW: ",Arr2)
print ("BUBBLE:",bubble_sort(Arr2[:]))
print ("SELECTION: ",selection_sort(arr=Arr2[:]))
print ("INSERTION: ",insertion_sort(arr=Arr2[:]))

print(insertion_sort([5,4,3,2]))
sorted(Arr2)
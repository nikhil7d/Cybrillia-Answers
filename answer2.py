def searchTri(arr, n):
    found = False
    for i in range(0, n-2):
       for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if (found == False):
        print(" Does not exist ")

arr = [] #List
n=int(input()) #Input array size
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
searchTri(arr, n)
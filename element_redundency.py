# Find the element redundency of an array.
# If the element in an array is repeted, count the repetaion of an element and print in the different array in same position. If there is no repetetion the print "0" in that position.
# Input = [1, 5, 2, 1, 2, 3, 1]
# Output = [2, 0, 1, 1, 0, 0]
# Take the user input

arr = []
n = int(input("Enter the size of the array: "))
for i in range(0, n) :
    ele = int(input())
    arr.append(ele)
arr1 = [0]*n

print("output :")

for i in range(0, n) :
    temp=0
    for j in range(i+1, n) :
        if (arr[i] == arr[j] and arr[i]!= -1) :
            temp = temp + 1
            arr[j]= -1
    if(temp!=0):
        arr1[i] = temp
    else :
        arr1[i] = 0
    print(arr1[i])
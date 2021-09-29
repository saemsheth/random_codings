#Merge sort

def merge_sort(n):
    #base case for recursion
    if len(n)<=1:
        return n

    #divide the list into two halves
    mid = len(n)//2
    left_side = n[:mid]
    right_side = n[mid:]

    #call the same function with the new lists
    merge_sort(left_side) 
    merge_sort(right_side)

    i = j = k = 0

    #compare left side elements with right side and place the smaller number amongst them in the result list
    while i< len(left_side) and j < len(right_side) :
        if left_side[i] <= right_side[j] :
            n[k] = left_side[i]
            i += 1
        else:
            n[k] = right_side[j]
            j +=1
        k += 1
    
    #put the remaining elements of the list in the result list
    while i<len(left_side):
        n[k] = left_side[i]
        i += 1
        k += 1

    while j<len(right_side):
        n[k] = right_side[j]
        j += 1
        k += 1

def main():
    n = [1,4,6,2,3,5]
    merge_sort(n)
    print(n)

main()
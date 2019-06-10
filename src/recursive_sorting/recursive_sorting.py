# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            result.append(arrA[left_index])
            left_index += 1
        else:
            result.append(arrB[right_index])
            right_index += 1

    result += arrA[left_index:]
    result += arrB[right_index:]
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

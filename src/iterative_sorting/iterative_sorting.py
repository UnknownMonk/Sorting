def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for cur_index in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[cur_index]:
                arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

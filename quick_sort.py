import random


def quick_sort(arr):
    if not arr:
        return arr
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n//2]
    left, right = 0, n-1
    while left < right:
        while arr[left] < pivot:
            left += 1
        while pivot < arr[right]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[:left] = quick_sort(arr[:left])
    arr[left+1:] = quick_sort(arr[left+1:])
    return arr


def quick_sort2(arr):
    if not arr or len(arr) <= 1:
        return arr
    left, right = [], []
    pivot = arr[(len(arr)-1) // 2]
    for v in arr:
        if v < pivot:
            left.append(v)
        elif pivot < v:
            right.append(v)

    arr = quick_sort2(left) + [pivot] + quick_sort2(right)
    return arr


def main():
    for _ in range(10):
        arr = list(range(13))
        random.shuffle(arr)
        print(f'Before: {arr}')
        sorted_arr = quick_sort(arr)
        assert (sorted_arr == sorted(arr))
        sorted_arr = quick_sort2(arr)
        assert (sorted_arr == sorted(arr))
        print(f'After: {arr}')


if __name__ == '__main__':
    main()

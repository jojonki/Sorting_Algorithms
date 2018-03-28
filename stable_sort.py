# sample input
# 5
# H4 C9 S4 D2 C3
import copy
N = int(input())
C = [{'m': i[0], 'v': int(i[1:])} for i in input().split(' ')]
C1 = copy.copy(C)
C2 = copy.copy(C)


def swap(d, a, b):
    tmp = d[a]
    d[a] = d[b]
    d[b] = tmp
    return d


def bubble_sort(N, A):
    swap_count = 0
    for i in range(N):
        crnt_swap_count = swap_count
        for j in reversed(range(i + 1, N)):
            if A[j-1]['v'] > A[j]['v']:
                swap(A, j-1, j)
                swap_count += 1
        if crnt_swap_count == swap_count: # no swap
            break
    return A


def selection_sort(N, A):
    for i in range(N):
        min_ind = i
        for j in range(i+1, N):
            if A[j]['v'] < A[min_ind]['v']:
                min_ind = j
        if i != min_ind:
            swap(A, i, min_ind)
    return A


def print_card(C):
    print(' '.join([i['m']+str(i['v']) for i in C]))


def is_stable(C1, C2):
    assert len(C1) == len(C2)
    for a, b in zip(C1, C2):
        if a != b:
            return False
    return True


# bubble_sort
b_sort = bubble_sort(N, C1)
print_card(b_sort)
print('Stable') # bubble sort is always stable

s_sort = selection_sort(N, C2)
print_card(s_sort)
if is_stable(b_sort, s_sort):
    print('Stable')
else:
    print('Not stable')

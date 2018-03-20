N = int(input())
A = [int(i) for i in input().split(' ')]


def swap(d, a, b):
    tmp = d[a]
    d[a] = d[b]
    d[b] = tmp
    return d


swap_count = 0
for i in range(N):
    minj = i
    for j in range(i, N):
        if A[j] < A[minj]:
            minj = j
    if i != minj:
        A = swap(A, minj, i)
        swap_count += 1

print(' '.join(map(str, A)))
print(swap_count)

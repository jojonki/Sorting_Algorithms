# A = [5, 3, 2, 4, 1]
# N = len(A)
N = int(input())
A = [int(i) for i in input().split(' ')]

swap_count = 0
i = 0
while True:
    crnt_swap_count = swap_count
    for j in reversed(range(i + 1, N)):
        if A[j-1] > A[j]:
            tmp = A[j]
            A[j] = A[j-1]
            A[j-1] = tmp
            swap_count += 1
    i += 1
    if crnt_swap_count == swap_count: # no swap
        break

print(' '.join(map(str, A)))
print(swap_count)

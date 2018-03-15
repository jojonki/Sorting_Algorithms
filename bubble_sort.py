# A = [5, 3, 2, 4, 1]
# N = len(A)
N = int(input())
A = [int(i) for i in input().split(' ')]

swap_count = 0
while True:
    crnt_swap_count = swap_count
    for i in reversed(range(1, N)):
        if A[i-1] > A[i]:
            tmp = A[i]
            A[i] = A[i-1]
            A[i-1] = tmp
            swap = True
            swap_count += 1
    if crnt_swap_count == swap_count: # no swap
        break

print(' '.join(map(str, A)))
print(swap_count)

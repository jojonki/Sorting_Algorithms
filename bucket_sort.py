import random

MIN   = int(input())
MAX   = int(input())
d_len = int(input())


def bucket_sort(data):
    buckets = [0] * (MAX - MIN + 1)
    offset = MIN
    for d in data:
        buckets[d - offset] += 1
    ret_data = []
    for i, b in enumerate(buckets):
        ret_data += [i + offset] * b
    return ret_data


if __name__ == '__main__':
    d = [random.randint(MIN, MAX) for _ in range(d_len)]
    print('original:', d)
    sorted_d = bucket_sort(d)
    print('sorted  :', sorted_d)

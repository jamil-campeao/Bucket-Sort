def bucket_sort(arr):
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]


    for num in arr:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)


    for bucket in buckets:
        bucket.sort()
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr
arr = [0.42, 0.32, 0.75, 0.12, 0.54, 0.28, 0.83]
sorted_arr = bucket_sort(arr)
print("Array ordenado:", sorted_arr)

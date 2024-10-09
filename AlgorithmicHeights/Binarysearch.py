import array

def BinarySearch(arr, keys):
    n = len(arr)
    indices = []
    for key in keys:
        low = 0
        high = n-1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == key:
                indices.append(mid+1)
                break
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        if low>high:
            indices.append(-1)
    print(" ".join(map(str, indices)))

file_path = input('Please enter path to your file: ')
with open(file_path, 'r') as file:
     n = int(file.readline())
     m = int(file.readline())
     content = file.readlines()
     all_numbers = " ".join(content).split()
     arr = [int(all_numbers[i]) for i in range(n)]
     keys = [int(all_numbers[n + i]) for i in range(m)]
BinarySearch(arr,keys)

def InsertionSort (file):
    length = int(file.readline())
    tosort = [int(x) for x in file.readline().split()]
    switches = 0
    for x in range(1, length):
        j = x-1
        key = tosort[x]
        while j>=0:
              if tosort[j]>key:
                 tosort[j+1]=tosort[j]
                 j-=1
                 switches+=1
              else:
                   break
        tosort[j+1]=key
    return switches


file_path = input('Please enter a path to your dataset :')
with open (file_path, 'r') as file:
     ShiftNumber=InsertionSort(file)
     print(ShiftNumber)

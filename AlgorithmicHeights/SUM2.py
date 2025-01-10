def SUM2 (file_path):
    with open (file_path, 'r') as file:
         lines = file.readlines()
         quantity, size = map(int, lines[0].split())
         

         for line in lines[1:]:
             arr = list(map(int, line.split()))
             indices_found = False

             value_to_index = {} 
             for i in range(size): 
                 check = arr[i]*-1 
                 if check in value_to_index: 
                      print(value_to_index[check] + 1, i + 1) 
                      indices_found = True 
                      break 
                
                 value_to_index[arr[i]] = i
                   
             if not indices_found:
                 print(-1)
              
file_path = input("Where are your datas?? ")
SUM2(file_path)

                    
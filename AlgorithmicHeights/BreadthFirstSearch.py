def is_connected 


def BFS (file_path):
    with open (file_path, 'r') as file:
         content = file.readlines()
         nodes, edges = map(int, content[0].split())
         distances = {}
         verteces = [1:nodes]
         
         start=1
 
         for line in content[1:]:
             line_el = line.split()
             if str(start) in line_el[0]:
                distances[line_el[1]] = 1
                if
                
                
         
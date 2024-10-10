def DegreeArray (file_path):
  with open(file_path, 'r') as file:
    first_line = file.readline().split()
    ver = int(first_line[0])
    Degrees = [0]*ver
    edges = int(first_line[1])
    for _ in range(edges):
        nodes = file.readline().strip().split()
        node1 = int(nodes[0])-1
        node2 = int(nodes[1])-1
        Degrees[node1]+=1
        Degrees[node2]+=1
  print(" ".join(map(str, Degrees)))

file_path = input('Please enter path to your file: ')
DegreeArray(file_path)
         

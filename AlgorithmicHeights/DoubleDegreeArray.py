def DDArray(file_path):
    with open (file_path, 'r') as file:
         first_line = file.readline().split()
         nodes = int(first_line[0])
         print(nodes)
         edges = int(first_line[1])
         print(edges)
         content = []
         for line in file:
             line = line.strip().split()
             content.extend(line)
         sorted_content = sorted(content)
         degrees = {i: 0 for i in range(1, nodes+1)}
         node_count = {}
         for node in sorted_content:
             node = int(node)
             if node in node_count:
                node_count[node] += 1
             else:
                node_count[node] = 1
         for node in node_count:
             degrees[node] = node_count[node]
         degrees_sum = {i: 0 for i in range(1, nodes+1)}
         for i in range(0, len(content), 2):
            current_node = int(content[i])
            neighbor_node = int(content[i + 1])
            degrees_sum[current_node] += degrees[neighbor_node]
            degrees_sum[neighbor_node] += degrees[current_node]
         for value in degrees_sum.values():
             print(value, end=" ")
file_path = input("Enter path to your data: ")
DDArray(file_path)

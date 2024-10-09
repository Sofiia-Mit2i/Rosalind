def square(a, b):
    c = (a**2) + (b**2)
    return c

with open('/home/sophia_iln/PythonPractice/rosalind_ini2_1_dataset.txt','r') as file:
     for line in file:
         values = line.split()
         a = int(values[0])
         b = int(values[1])
         result = square (a,b)
         print (f'for a={a} and b={b}: result={result}')

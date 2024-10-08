def SumOddNum (a,b):
    if a < b < 10000:
       odds = []
       i = 0 
       if a%2 == 0:
          a += 1
       for num in range (a,b+1,2):
           i = i + num
           odds.append(i)

       return odds[-1]
    else:
          return [] 

with open ('/home/sophia_iln/Rosalind/rosalind_ini4.txt','r') as file:
     values = file.readline().split()
     a = int(values[0])
     b = int(values[1])
     result = SumOddNum (a,b)
     print (f'for a={a} and b={b}: result={result}')

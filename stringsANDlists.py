def slice(s, a, b, c, d):
    if len(s) <= 200:
       print(s[a:b+1])
       print(s[c:d+1])
       return s[a:b+1],s[c:d+1] 
with open ('/home/sophia_iln/Rosalind/rosalind_ini3.txt','r') as file:
     s = file.readline()
     values = file.readline().split()
     a = int(values[0])
     b = int(values[1])
     c = int(values[2])
     d = int(values[3])
     result = slice (s,a,b,c,d)
     print(f'Your words are: {result}')

def EvenLines ():
    file = input('Enter path to your file: ')
    file_path = '/home/sophia_iln/Rosalind/EvenFile.txt'
    with open (file, 'r') as file:           
         with open ('/home/sophia_iln/Rosalind/EvenFile.txt', 'w') as NewFile:
              for index,line in enumerate(file):
                  if (index + 1) % 2 == 0:
                     NewFile.write(line)
    return file_path

EvenLines()
  
                     

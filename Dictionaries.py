def occ ():
    file = input('Please enter path to your file: ')
    word_count = {}
    i = 1
    with open (file, 'r') as file:
         content = file.read()
         words = content.split()
         for word in words:
             if word in word_count:
                word_count[word] += 1
             else:
                 word_count[word] = 1
    sorted_dict_by_value = dict(sorted(word_count.items(), key=lambda item: item[1]))
    for word, count in sorted_dict_by_value.items():
        print (f'{word} {count}')

occ()


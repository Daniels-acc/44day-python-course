# Transforming the strings using list comprehension

filenames = ['1.doc', '1.report', '1.presentation']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

for x in filenames:
    file = open(x, 'w')
    # y = file.write(x) only if we want to write in file
    file.close()

print(filenames)
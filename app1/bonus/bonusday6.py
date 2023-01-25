contents = ['something crazy happening',
            'random blablabal',
            'third paragraph']
filenames = ['doc.txt', 'presentation.txt', 'report.txt']

for content, filename in zip(contents, filenames): # loop through
    file = open(f"bonus-files/{filename}", 'w')
    file.write(content)

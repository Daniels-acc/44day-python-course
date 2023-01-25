files = ['random1', 'random2', 'random3', 'random4']

for file in files:
    file = open(f"src/{file}", 'w')
    file.write("Yeeeahello")
    file.close()
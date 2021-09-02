filename = 'pi_digits.txt'
with open(filename) as file_object:
    # contents = file_object.read()
    for line in file_object:
        print(line.rstrip())
#print(contents.rstrip())

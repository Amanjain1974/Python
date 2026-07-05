file1 = open('my_file.txt','r+')
writing_file = file1.write('hello I am Aman Jain')
print(writing_file)

file1.close()

file1 = open('my_file.txt','r+')
reading_file = file1.read()
print(reading_file)

file1.close()
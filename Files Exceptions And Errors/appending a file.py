file1 = open('my_file.txt','a')
appending_file = file1.write('hello I am Aman Jain')

file1.close()

file1 = open('my_file.txt','r')
reading_file = file1.read()
print(reading_file)

file1.close()




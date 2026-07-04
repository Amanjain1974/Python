a =input('Enter Text to write to the file :')
print('Data Successfully Wriiten to Output.txt\n\n')

file1 = open('output.txt','w')
writing_file = file1.write(a)
print(writing_file)

file1.close()

b=input('Enter Addition Text To append :')

file1 = open('output.txt','a')
appending_file = file1.write(b)
file1.close()

print('\nData Successfully Appended\n')

print('Final Content of output.txt:\n')

file1 = open('output.txt','r')
reading_file = file1.read()
print(reading_file)

file1.close()





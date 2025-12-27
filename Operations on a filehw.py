#open file and read its content
file = open('Codingal.txt', 'r')
print(file.read())
file.close()

#open file and read its beginning 10 characters
file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(10))
file.close()

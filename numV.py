s = 'kgjdoirtureklnvdlkcvnwpeofj'
numV = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numV += 1
print('Number of vowels is: ' + str(numV))

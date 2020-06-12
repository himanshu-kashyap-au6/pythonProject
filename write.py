order = int(input())

#   For writing the matrix in inputFile
out = open('inputFile.txt', 'w')
for i in range(order):
    b = input()
    out.write(b)
    out.write('\n')
out.close()

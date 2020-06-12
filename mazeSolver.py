import argparse
import mazesolverhk


parser = argparse.ArgumentParser()
#   i stands for inputFile
parser.add_argument('--i', type=str)
#   o stands for outputFile
parser.add_argument('--o', type=str)
#   s stands for source vertex
parser.add_argument('--s', type=str)
#   d stands for destination vertex
parser.add_argument('--d', type=str)
args = parser.parse_args()

#   Creating and instance of class Graph imported from mazesolverhk
g = mazesolverhk.Graph()

#   For opening the inputFile in read mode
inp = open(args.i, 'r')
strArr = inp.readlines()
order = len(inp.readlines())
arr = []
for i in strArr:
    arr.append(list(map(int, i.rstrip().split())))
inp.close()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        #  Condition to check if the element present left to
        # the current element and the current element
        # in the same row both are 1 or not
        if (j-1 >= 0 and arr[i][j-1] == 1 and
                arr[i][j] == 1):
            g.addEdge((i, j-1), (i, j))
        #  Condition to check if the element present just above the
        #  current element and the current element
        #  in the same column both are 1 or not
        if (i-1 >= 0 and arr[i-1][j] == 1 and
                arr[i][j] == 1):
            g.addEdge((i-1, j), (i, j))

#   Condition to check if the user provides
#   the source vertex in command or not.
if (args.s is not None):
    a = args.s
#   If not then 0,0 will be the default source vertex
else:
    a = '0,0'
#   Condition to check if the user provides
# the destination vertex in command or not.
if (args.d is not None):
    b = args.d
# If not last element of last column will be the default destination vertex.
else:
    b = str(len(arr)-1)+','+str(len(arr[0])-1)

resultList = g.sourceToDest(tuple(map(int, a.split(","))),
                            tuple(map(int, b.split(","))))

if resultList != -1:
    outputList = [[0 for i in range(len(arr[i]))] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            #   Condition to check if the vertex is present in resultList.
            if (i, j) in resultList:
                outputList[i][j] = 1
elif resultList == -1:
    outputList = -1

#   Opening the output file in write mode
out = open(args.o, 'w')
if outputList != -1:
    for i in outputList:
        s = ""
        for j in i:
            s += str(j)+" "
        out.write(s)
        out.write("\n")
    out.close()
elif outputList == -1:
    s = '-1'
    out.write(s)
    out.write("\n")
    out.close()

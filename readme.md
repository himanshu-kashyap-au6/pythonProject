<div align="center">

#   __Maze Solver__

</div>

*   #  __Aim:__
    ## The aim of this project is to build a python program that runs as a command-line tool. It should take the input and output file name as command-line arguments. Using the square matrix present in the input file it should generate a path to reach from source to the destination point of the maze and put it in the output file. If the maze is unsolvable, it should return -1 as the only value in the output file.
    ## In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. 

*   #   __How to solve the problem__
    *   ##  Read the input matrix from the inputFile.txt and form a 2-D mtrix from it.
    *   ##  In the given 2-D matrix cosider the position of the element as node where 1 is present and make a graph from it.
    *   ##  Now check whether it is possible to reach from source to destination in the 2-D matrix with the help of 1's
    *   ##  If yes find the position of all the 1's present in 2-D array and store them in a list say resultArray.
    *   ## Create another 2-D array say outputList and make each position which is present in resultArray as 1 and rest of the position as 0
    *   ##  Write the outputList in the outputFile.txt

*   #   __Concepts used to implement the solution__
    *   ##   File handling
    *   ##   Graph
    *   ##   BFS
    *   ##   Dijkstra

*   #   __Description__
    ##   Folder mainly contains four files:
    1.     inputFile.txt   
    1.     outputFile.txt   
    1.     mazeSolver.py   
    1.     write.py   
    
##  __write.py__
---
*   ### It will request for an intput which will be the order of the matrix say n
*    ### It will open the inputFile.txt in write mode
*    ### It will request for input n times and user needs to give the space seperated input with 0 or 1
*    ### It will write the each input in inputFile.text and then close the file

##  __inputFile.txt__
---
*   ### inputFile.txt will contain an nxn matrix with 0 and 1 as element

##  __outputFile.txt__
---
*   ### outputFile.txt will contain an nxn matrix with 0 and 1 as element but 1 will present at source to destination path only or -1.

##   __mazeSolver.py__
---
*   ### import two modules
    *   ####    argparse
    *   ####    mazesolverhk
*   ### argparse: this module is used for creating command-line
*   ### mazesolverhk: this is an custom module in oreder to import this module user must run a command "pip install mazesolverhk"
    *   ### mazesolverhk contains a class Graph and it includes four functions.
        * addEdge
        * pathExist
        * dijkstra
        * sourceToDest
        ### The whole code of this class is present in the __init.py__ in the mazesolverhk folder which is again present in mazesolverhk folder present in same directory.
        ### All these functions are explained below:

    ##   addEdge:
    ---
    ### This function required two arguments u and v.
    ### As an undirected graph is getting creating it will add u as key to the graph which is define in constructor and append v in list as value of u and vice versa for v and u.

    ##  pathExist:
    ---
    ### This function also requires two arguments u and v
    ### Where u is source and v is destination
    ### This function working on the principle of __BFS__

    #   Breadth First Search(BFS):
    ### BFS is a traversing algorithm it works in the following manner

<div align="center">

![BFS logo](https://media.geeksforgeeks.org/wp-content/uploads/binary-Graph.png)
</div> 
<div align="center">
figure 01
</div>

###  Let's say we have a graph as shown in figure 01 and we need to findout whether a path exist between 0 and 8 or not so we will start from any node 0
*   ### It will create a queue say Q = [] 
    ### It will create a dictionary say visted = {} and add each node as key with their value as false so visited become
    ### visted = {0: false, 1: false, 2: false, 3: false, 4: false,5: false, 6: false, 7: false, 8: false}
*   ### It will enque the stating node to queue and mark the starting node as true in visted List now the Q and visted will become
    ### Q = [0]
    ### visited = {0: true,1: false, 2: false, 3: false, 4: false,5: false, 6: false, 7: false, 8: false}
*   ### Now it will dequeue the Q and enque the nodes which are connected to node 0 and mark those node as visted
    ### Now the Q = [1,7] and 
    ### visited = {0: true, 1: true, 2: false, 3: false, 4: false, 5: false, 6: false, 7: true, 8: false}
*   ### Again it will dequeu the 1 so the Q becomes: Q = [7]    
    ### Now it will explore node 1 and enqueue the nodes which as not visted and mark them as visited so the Q and visited beome:
    ### Q = [7,2]
    ### visited = {0: true, 1: true, 2: true, 3: false, 4: false, 5: false, 6: false, 7: true, 8: false}
*   ### Now 7 will be dequeued so the Q = [2]
    ### It will explore 7 now and enqueue the unvisited nodes and mark them as visited therefor
    ### Q=[2,8,6]
    ### visited = {0: true, 1: true, 2: true, 3: false, 4: false, 5: false, 6: true, 7: true, 8: true}
*   ### Now 2 will get dequeued therefor Q = [8, 6]
    ### It will explore 2 and enqueu the unvisited node and mark them as visited therefor   
    ### Q = [8, 6, 3, 5]
    ### visited = {0: true, 1: true, 2: true, 3: true, 4: false, 5: true, 6: true, 7: true, 8: true}
*   ### Now 8 will get dequeued i.e Q = [6, 3, 5] and nothing will chnage in Q and visted as all the nodes connected to 8 are already visited therefor
    ### Q = [6, 3, 5]
    ### visited = {0: true, 1: true, 2: true, 3: true, 4: false, 5: true, 6: true, 7: true, 8: true}
*   ### As the dequeued node is our destination node so we can conclude that there is path exist between source to destination therefor it return True. If it will be unable to find the destination element it will return False.

#     __Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm):__
---
### It is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

##  Hoe it works:
### Let distance of start vertex from satrt vertex is 0.
### Let distance of all other vertices from start is infinite or a very large no. say 10**9

##  Repeat
*   ### visit the unvisited vertex with the smallest known distance from start vertex
*   ###  For the current vertex examine its unvisited neighbours
*   ### For the current vertex calculate distance of each neighbour from start vertex.
*   ### If the calculated distance of  vertex is less than the known distance, update the shortest disatnce.
*   ### Update the previous vertex of the updated distances
*   ### Add the current vertex to the list of visited vertices
##  until all vertices visited.
##  Let's make it more clear with the help of an example.

<div align="center">

![Dijkstra logo](https://res.cloudinary.com/dyffrpmjj/image/upload/v1591502561/rqc6oabr80vtsiqo06se.png)
</div> 
<div align="center">
figure 02
</div>

### consider the simple graph shown in figure 02 let's say we want to find the shortest path from node A to every other nodes
### It will create a list say visited with all the nodes as key and  thier value as False and an another dictionary for storing vrevious vertex. and that is shown with the help of table below:
### In the table the shortest distance from A to A is 0 and rest of the distance say infinite or a very large number therefor the table becomes:
| Previous vertex | Vertex | Shortest distance from A |
|:----------:|:-------------:|:------:|
|  | A | 0     |
|  | B | 10**9 |
|  | C | 10**9 |
|  | D | 10**9 |
|  | E | 10**9 |

### Now it will vist to unvisted neighbour of vertex A and update the shortest distace from A and it will add the node A as True in visited dictionary therefor the table becomes:
| Previous vertex | Vertex | Shortest distance from A |
|:----------:|:-------------:|:------:|
|   | A | 0     |
| A | B | 6     |
|   | C | 10**9 |
| A | D | 1     |
|   | E | 10**9 |

### Now it check for minimum distance from previous vertex and repeat the algoruthm So we have minimum distance with D with shortest distance from A as 1, D have its neighbour as B and E.
### As we have find the distance from A to B as 6 but this time the distance between D to B is 2 and Distance of D from A is 1 so 1+2=3<6 therefor we will update the column B with previous vertex as D and shortest distance as 3 and D is updated as True in the visited dictionary therefor the table becomes:
| Previous vertex | Vertex | Shortest distance from A |
|:----------:|:-------------:|:------:|
|   | A | 0     |
| D | B | 3     |
|   | C | 10**9 |
| A | D | 1     |
| D | E | 2     |

### As we are at D and its neighbours are B and E but the minimum distance present is between D and E so the next vertex be E.
### E also have two neighbour B and C  and there distance will be From E to B is 2+2 = 4 and E to C is 2+5=7
### As distance Via E to B is 4 and via D is 3 so no need to update that we only need to update C row as 7<10**9 and E is updated as True in visted dictionary therefor the table becomes:
| Previous vertex | Vertex | Shortest distance from A |
|:----------:|:-------------:|:------:|
|   | A | 0 |
| D | B | 3 |
| E | C | 7 |
| A | D | 1 |
| D | E | 2 |

### Now E has two neighbours B and C And the minimum distance is present between E and B.
### Now the current vertex be B and its unvisited vertex is C and distance will become 3+5=8 but we have distance via E as 7 so no need to update now the B is updated as True in visited dictionary and the current vertex will become C it has no unvisited vertex so no need to change the table and C is updated as True in the visited dictionary. 
### Hence we found out the shortest distance from A to all the verteices with thier minimu distance and previous vertices stored in the dictionaries.

#  sourceToDest:

### It is a very simple function it take two arguments one is source and other is destination.
### It firstly check whether a path exist between source to destination or not.
### If the path exist It create a list source to destination firstly is append the destination to list it insert the previous elements received via dijkstra to the list in the begining and when it reaches to source it breaks the loop and return the sourcetodest list.
### If the path doesn't exist between source to destination point it simply returns -1.

#   Now coming back to mazeSolver.py:
*   ##  It import the argparse to fulfil the requirement of the project i.e. to enable command-line parsing.
*   ##  It will be requiring four arguments inputFile, outputFile, source and destination.
*   ##  It will create an instance g for the graph.
*   ##  Now it open the inputFile in read mode and calculate the total no. of lines present in the inputFile and close the file.
*   ##  Now it will again open the input file read all the lines one by one. The lines will be in the form of string it will conver them into the list of integers and form a 2-D list.
*   ##  Now it will form a graph from the 2-D list with the help of addEdge function.
*   ##  Now it will run the function source to destination to check whether they are connected or not if yes the what are the connecting vertices.
*   ##  Now it will again form another -D list with all elements as 1 for the positions which are present in sourcetodestination list and rest as 0.
*   ##  Now it will open the outputfile in write mode and wirte the 2-D list in outputfile if the path exist or -1 only if path doesn't exist.

#   __How to run the project:__
*   ### Open the terminal and run
>   ##   pip install mazesolverhk
*   ### Open the pythonProject folder and open the inputFile.txt.
*   ### Write an nXn matrix with 0 or 1 as element Or user can open the terminal go to pythonProject directory and run the command
    >    ##  python write.py
*    ###    Now we need to provide the order of the matrix say 4 or 3 etc.
*   ### Then Agin it will ask for inputs times of number entered and we need to provide sapce seperated n(entered number) value with 0 or 1
*   ### Now open the termina and go to the pythonProject directory if you are not in the pythonProject directory.  
### Now run the command 
>   ##  python mazeSolver.py --i=inputFile.txt --o=outputFile.txt --s=0,0 --d=3,3

*   ### Now open the outputFile.txt you will find the result to be printed over there.

#   __How to create pip package:__
*   ##  Create an account on pypi.org
*   ##  create a folder say myfirstpackage
*   ##  create another folder inside it say myfirstpackage
*   ##  create three more files in the root folder 
    *   ###    setup.py
    *   ###    readme.txt
    *   ###    License.txt

*   ## setup.py:
    ### It mainly contains the setup like name of package, version, description, author, packages, install requires

*    ##  readme.txt:
     ###    As the name suggesting this files contains the discription about the object.

*   ##  Now create one file with name __init__.py inside the folder that we have create inside the root folder and we will write our actual code whether it's a class or a fuction etc.

*   ##  Now open the terminal and run two commands 
>   ##  pip install wheel
>   ##  pip install twine
*   ##  Now we need to go to the directory of the root folder and run another command
>   ##  python setup.py sdist bdist_wheel
*   ##  And one more command
>   ##  twine upload dist/*
*   ##  provide the credetials and it will create the package successfully.

*   #   __Tools:__
    *   ##  Python
    *   ##  Github

*   #   __Refernces:__
    *   ##  BFS: https://youtu.be/pcKY4hjDrxk  
    *   ##  Dijksta: https://youtu.be/pVfj6mxhdMw
    *   ##  Command-line parsing: https://youtu.be/0twL6MXCLdQ
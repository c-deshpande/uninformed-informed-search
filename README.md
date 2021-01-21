# uninformed-informed-search
An algorithm implemented in Python which finds route between two cities.

Project done as part of CSE-5360 Artificial Intelligence course at UTA.

<p align="justify">This project implements two algorithms, Uniform Cost Search for doing uninformed search and A* algorithm for doing informed search.</p>

Problem statement is as follows,

<p align="justify">The program will compute a route between the origin city and the destination city, and will print out both the
length of the route and the list of all cities that lie on that route. It should also display the number of nodes
expanded and nodes generated.</p>

<p align="justify">The input file will have "END OF INPUT" at the end of the file to indicate the end of the file. Each city will be a single word.</p>

```
An example of the input format,
Luebeck Hamburg 63
Hamburg Bremen 116
Hamburg Hannover 153
Hamburg Berlin 291
Bremen Hannover 132
END OF INPUT

An example of the Heuristic file format,
Luebeck 300
Hamburg 200
Hannover 100
Berlin 200
Bremen 200
```

The program will take the following command line arguments,

```
find_route input_filename origin_city destination_city heuristic_filename

An example command line is:
find_route input1.txt Bremen Kassel (For doing Uninformed search)
or
find_route input1.txt Bremen Kassel h_kassel.txt (For doing Informed search)
```

If heuristic is not provided, the program does uninformed search by default. 

```
find_route input1.txt Bremen Kassel

should have the following output:

nodes expanded: 12
nodes generated: 20
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km

and

find_route input1.txt London Kassel

should have the following output:

nodes expanded: 7
nodes generated: 7
distance: infinity
route:
none

and

find_route input1.txt Bremen Kassel h_kassel.txt

should have the following output:

nodes expanded: 3
nodes generated: 8
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
```

GatorTaxi
GatorTaxi is a ride-sharing service software that manages pending ride requests efficiently using advanced data structures. This project was developed as part of the COP 5536 - Advanced Data Structures course.

Problem Statement
GatorTaxi receives numerous ride requests each day, each characterized by a unique ride number, estimated cost, and total trip duration. The software aims to efficiently manage these ride requests, supporting operations such as:

Printing a specific ride.
Printing a range of rides.
Inserting a new ride.
Getting the next ride with the least cost.
Canceling a ride.
Updating the trip duration of a given ride.
Data Structures Used
Min-Heap: Stores rides using the ride cost as the key, allowing quick access to the ride with the minimum cost.
Red-Black Tree (RBT): Stores rides using the ride number as the key, enabling efficient search, insert, and delete operations.
Files
gatorTaxi.py - The main driver code for the GatorTaxi service. It reads instructions from an input file provided by the user and performs one of the six functionalities based on the instruction.

minheap.py - Implements a Min-Heap data structure to store rides using ride cost as the key.

RBTree.py - Implements a Red-Black Tree (RBT) to store rides using the ride number as the key. Nodes in the RBT maintain a pointer to the position (index) of the ride in the Min-Heap.

filewriter.py - Handles writing the output to output_file.txt.

Instructions to Run
Place the input text file with the instructions in the same directory as the project files.

Run the following command in the terminal to execute the program and generate output_file.txt:

python gatorTaxi.py <inputfilename.txt>

The program will read the instructions from the input file, execute them, and write the output to output_file.txt.

Function Prototypes and Program Structure

gatorTaxi.py
insert(heap, ridenumber, ridecost, tripduration): Inserts a ride into the heap.
getnextride(heap): Retrieves the next ride with the minimum cost.
cancelride(heap, ridenumber): Cancels a ride based on the ride number.
printride(heap, ridenumber): Prints details of a specific ride.
printrides(heap, ridenumber1, ridenumber2): Prints all rides within a given range.
updatetrip(heap, ridenumber, new_tripduration): Updates the trip duration of a specific ride.

minheap.py
MinHeap class: Implements the Min-Heap data structure with methods to insert, delete, and retrieve rides.
Methods include: insert(triplet), getnextride(), deleteride(ridenumber), printride(ridenumber), printrides(ridenumber1, ridenumber2), update(ridenumber, tripduration).
RBTree.py
RBT class: Implements the Red-Black Tree data structure with methods for insertion, deletion, and searching rides.
Node class: Represents each node in the Red-Black Tree.
Methods include: insert(ridenumber, ridetriplet), delete(ridenumber), find(ridenumber), update_tripduration(ridenumber, newtripduration), printrides(ridenumber1, ridenumber2).

filewriter.py
File class: Handles writing output to output_file.txt.
Methods include: filewrite(data).

Time and Space Complexity Analysis

Time Complexity:

Insert: O(log n)
CancelRide: O(log n)
Printride: O(log n)
Printrides: O(s + log n), where s is the number of rides in the range.
getnextride: O(log n)
UpdateTrip: O(log n)

Space Complexity:
Red-Black Tree: O(n)
Min-Heap: O(n)

# GatorTaxi

GatorTaxi is a ride-sharing service software designed to efficiently manage pending ride requests using advanced data structures. This project is part of the COP 5536 - Advanced Data Structures course.

For more details, please read GatorTaxi.pdf

## Problem Statement

GatorTaxi receives multiple ride requests daily, each characterized by a unique ride number, estimated cost, and total trip duration. The objective is to manage these ride requests effectively by implementing operations such as:

- Printing a specific ride.
- Printing a range of rides.
- Inserting a new ride.
- Getting the next ride with the lowest cost.
- Canceling a ride.
- Updating the trip duration for a given ride.

## Data Structures Used

- **Min-Heap**: Stores rides with the ride cost as the key to quickly retrieve the ride with the minimum cost.
- **Red-Black Tree (RBT)**: Stores rides using the ride number as the key, facilitating efficient search, insert, and delete operations.

## Project Files

- `gatorTaxi.py` - The main driver script for the GatorTaxi service. Reads instructions from an input file and executes one of the six core functionalities based on the instructions.
- `minheap.py` - Implements the Min-Heap data structure, where rides are stored with the ride cost as the key.
- `RBTree.py` - Implements the Red-Black Tree (RBT) data structure, where rides are stored with the ride number as the key. Each node maintains a pointer to its position in the Min-Heap.
- `filewriter.py` - Handles writing outputs to `output_file.txt`.

## How to Run

1. Place the input text file containing the ride instructions in the same directory as the project files.
2. Run the following command in the terminal to execute the program:

   ```bash
   python gatorTaxi.py <inputfilename.txt>

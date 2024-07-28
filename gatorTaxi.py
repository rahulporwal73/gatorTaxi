from minheap import MinHeap
from filewriter import File
import sys     

# define function to insert a ride into heap which is an instance of MinHeap
def insert(heap,ridenumber,ridecost,tripduration):
    #The ride triplet is inserted in heap
    #heap represents a data structure in which the ride is inserted in both minheap and red black tree 
    heap.insert((ridenumber,ridecost,tripduration)) 
    return heap

# function to get the next ride from the heap
# next ride will be the ride with the lowest cost 
def getnextride(heap):
    if heap.get_number_of_active_rides() == 0: #if there are no rides available in the heap, print no active ride requests
        data = ["No active ride requests"]
        out_file.filewrite(data)
        print("No active ride requests")
        return
    next_ride = heap.getnextride()
    
    output = ""
    output=output+"("+str(next_ride["ride"][0])+","+str(next_ride["ride"][1])+","+str(next_ride["ride"][2])+")"  
    data = [output]
    out_file.filewrite(data) # write output to output_file.txt
    print(output)
    
#function to delete a ride from the heap (effectively deletes the ride from both minheap and red black tree)
def cancelride(heap,ridenumber):
    if heap.get_number_of_active_rides() == 0:
        return
    heap.deleteride(ridenumber)
    
#function to print a ride with given ridenumber
def printride(heap,ridenumber):
    if heap.get_number_of_active_rides() == 0:
        data = ["(0,0,0)"]
        out_file.filewrite(data)
        print("(0,0,0)")
        return
    heap.printride(ridenumber)

#function to print all rides between ridenumber1 and ridenumber2
def printrides(heap,ridenumber1,ridenumber2):
    if heap.get_number_of_active_rides() == 0:
        data = ["(0,0,0)"]
        out_file.filewrite(data)
        print("(0,0,0)")
        return
    heap.printrides(ridenumber1,ridenumber2)
    
#function to update trip duration of a ride, given its ride number
def updatetrip(heap,ridenumber,new_tripduration):
    if heap.get_number_of_active_rides() == 0:
        return
    heap.update(ridenumber,new_tripduration)
    

#read input filename given by user as a commandline argument
try:
    inputfilename = sys.argv[1]
except:
    exit()

#open input file in read mode if it exists
try:
    inputfile = open(inputfilename,'r')
except:
    exit()

#creating an instance of MinHeap()
heap=MinHeap()
out_file = File() #creating an instance of File() to write output to 
instructions = inputfile.readlines()  #reading instructions from input file
for instruction in instructions:
    #instruction for Insert(ridenumber,ridecost,tripduration)
    if instruction.startswith("Insert"):
        command = instruction[instruction.find('(')+1:instruction.find(')')]
        cmd = command.split(',')
        ridenumber = int(cmd[0])
        ridecost = int(cmd[1])
        tripduration = int(cmd[2])
        insert(heap,ridenumber,ridecost,tripduration)
    #instruction for Print(ridenumber),Print(ridenumber1,ridenumber2)
    elif instruction.startswith("Print"):
        #instruction for Print(ridenumber1,ridenumber2)
        if instruction.count(",") == 1:
            command = instruction[instruction.find('(')+1:instruction.find(')')]
            cmd = command.split(',')
            ridenumber1 = int(cmd[0])
            ridenumber2 = int(cmd[1])
            printrides(heap,ridenumber1,ridenumber2)
        #instruction for Print(ridenumber)
        elif instruction.count(",") == 0:
            cmd = instruction[instruction.find('(')+1:instruction.find(')')]
            ridenumber = int(cmd)
            printride(heap,ridenumber)
    #instruction to Updatetrip(ridenumber,new tripduration)
    elif instruction.startswith("UpdateTrip"):
        command = instruction[instruction.find('(')+1:instruction.find(')')]
        cmd = command.split(',')
        ridenumber = int(cmd[0])
        new_tripduration = int(cmd[1])
        updatetrip(heap,ridenumber,new_tripduration)
    #instruction for getnextride()
    elif instruction.startswith("GetNextRide"):
        getnextride(heap)
    #instruction to cancel a ride
    elif instruction.startswith("CancelRide"):
        cmd = instruction[instruction.find('(')+1:instruction.find(')')]
        ridenumber = int(cmd)
        cancelride(heap,ridenumber)
    
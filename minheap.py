from RBTree import RBT
from filewriter import File
class MinHeap:
    def __init__(self):
        self.heap = []  #storing minheap in a list. The key is ride cost.
        self.size=0
        self.rbt = RBT()  #creating an instance of a red black tree. RBT stores rides using ridenumber as key
        self.outputfile = File() #creating an instance of File() to write outputs to output_file.txt
    # gets parent of node which is stored at position i in minheap
    def parent(self, i):
        return (i-1)//2
    # gets left child of node which is stored at position i in minheap
    def leftchild(self,i):
        return (2*i+1)
    # gets right child of node which is stored at position i in minheap
    def rightchild(self,i):
        return (2*i+2) 
    #gets number of active rides in the heap that is, size of heap
    def get_number_of_active_rides(self):
        return len(self.heap)
    #inserts triplet in self.heap and self.rbt
    #after inserting node, heapify 
    def insert(self, triplet):
        check_duplicate,_ = self.rbt.find(triplet[0])
        if check_duplicate is not None:
            data = ["Duplicate RideNumber"]
            self.outputfile.filewrite(data)
            print("Duplicate RideNumber")
            exit()
        data = {"ride":None,"pointer":None} # storing ridetriplet and pointer to locate the ride in red black tree in data as a dictionary
        data["ride"] = triplet
        data["pointer"]=triplet[0] #we can locate nodes in red black tree using ridenumber since ridenumbers are the keys in red black tree and theya re all unique
        self.heap.append(data)#inserting into min heap at leaf, updating pointer to red black tree to the ridenumber
        self.size+=1 # as we added a node to minheap, size of heap increases
        i = len(self.heap)-1
        self.rbt.insert(triplet[0],triplet)   #inserting ride into red black tree
        self.rbt.update_pointer(triplet[0],i) #sending position of the ride triplet in the heap to update pointer of the ride in red black tree.
        #heapify if cost of node added is smaller than its parent or if cost is same as parent but trip duration is lesser, then swap position with parent
        # after each heapify iteration, update pointers of nodes being swapped, in the red black tree
        while i>0:
            if (self.heap[self.parent(i)]["ride"][1] > self.heap[i]["ride"][1]) or (self.heap[self.parent(i)]["ride"][1] == self.heap[i]["ride"][1] and self.heap[self.parent(i)]["ride"][2] > self.heap[i]["ride"][2]):
                self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]
                self.rbt.update_pointer(self.heap[self.parent(i)]["ride"][0],self.parent(i))
                self.rbt.update_pointer(self.heap[i]["ride"][0],i)
                i = self.parent(i)
            else:
                break
    #gets next ride from the heap and deletes it from heap.
    # next ride is ride with minimum cost. in a minheap, node with minimum key is at [0] index
    def getnextride(self):
        next_ride = self.heap[0]
        self.deleteride(next_ride["ride"][0])
        return next_ride

    # deletes ride from minheap and red black tree
    def deleteride(self,ridenumber):
        #checks if ridenumber to delete exists or not. 
        #If ride exists, returns the position(index) of ride in minheap
        ride_to_delete,idx = self.rbt.find(ridenumber) 
        if ride_to_delete is None:
            return 
        #deletes ride from red black tree
        self.rbt.delete(ridenumber)  
        #deleting ride from minheap 
        tmp = self.heap[idx]
        self.heap[idx] = self.heap[-1]
        self.heap[-1] = tmp
        self.rbt.update_pointer(self.heap[idx]["ride"][0],idx)
        self.heap.pop()
        self.size-=1
        # heapify to ensure minheap property is maintained
        while True:
            leftchild = self.leftchild(idx) # left child of node
            rightchild = self.rightchild(idx) #ridght child of node
            smallest = idx
            #if left child has lesser cost
            if leftchild < len(self.heap) and self.heap[leftchild]["ride"][1] < self.heap[smallest]["ride"][1]: 
                smallest = leftchild
            #if left child has same cost but lesser trip duration
            elif leftchild < len(self.heap) and self.heap[leftchild]["ride"][1] == self.heap[smallest]["ride"][1] and self.heap[leftchild]["ride"][2]<self.heap[smallest]["ride"][2]:
                smallest = leftchild
            #if right child has lesser cost
            if rightchild < len(self.heap) and self.heap[rightchild]["ride"][1] < self.heap[smallest]["ride"][1]:
                smallest = rightchild
            #if right child has same cost but lesser trip duration
            elif rightchild < len(self.heap) and self.heap[rightchild]["ride"][1] == self.heap[smallest]["ride"][1] and self.heap[rightchild]["ride"][2]<self.heap[smallest]["ride"][2]:
                smallest = rightchild
            # we check if minheap property was violated with any of the 2 children
            if smallest != idx:
                tmp = self.heap[idx]
                self.heap[idx] = self.heap[smallest]
                self.heap[smallest] = tmp
                # update pointers in red black tree to new positions of the rides being swapped in minheap
                self.rbt.update_pointer(self.heap[idx]["ride"][0],idx)  
                self.rbt.update_pointer(self.heap[smallest]["ride"][0],smallest)
                idx = smallest
            else:
                break
            
    #prints the ride if it exists. otherwise prints (0,0,0)
    def printride(self,ridenumber):
        ride,_ = self.rbt.find(ridenumber) #checking if ride exists
        if ride is None:
            data = ["(0,0,0)"]
            self.outputfile.filewrite(data)
            print("(0,0,0)") #if ride does not exist
            return
        output = ""
        output=output+"("+str(ride[0])+","+str(ride[1])+","+str(ride[2])+")"  
        data = [output]
        self.outputfile.filewrite(data) # prints ride if it is found
        print(output)

    #prints all rides within [ridenumber1,ridenumber2] interval
    def printrides(self,ridenumber1,ridenumber2): 
        self.rbt.printrides(ridenumber1,ridenumber2) # we print the ride by searching them in red black tree 

    #updatetrip(ridenumber,new trip duration) function implementation
    def update(self,ridenumber,new_tripduration):
        existing_ride,idx = self.rbt.find(ridenumber) #search for ride in red black tree by searching for ridenumber
        if existing_ride is None:
            return
        old_tripduration = existing_ride[2]
        if new_tripduration <= old_tripduration:
            #if new trip duration is less than old trip duration, we simply replace old trip duration with new trip duration
            # update trip duration in both rbt and minheap
            # check if parent of ride has same cost but its trip duration is more than new trip duration of existing ride
            # if it is, then swap the rides and update pointers in rbt
            new_node = (self.heap[idx]["ride"][0],self.heap[idx]["ride"][1],new_tripduration)
            self.heap[idx]["ride"] = new_node
            self.rbt.updatetripduration(ridenumber,new_tripduration)
            while idx>0:
                if (self.heap[self.parent(idx)]["ride"][1] == self.heap[idx]["ride"][1] and self.heap[self.parent(idx)]["ride"][2] > self.heap[idx]["ride"][2]):
                    self.heap[idx],self.heap[self.parent(idx)] = self.heap[self.parent(idx)],self.heap[idx]
                    self.rbt.update_pointer(self.heap[self.parent(idx)]["ride"][0],self.parent(idx))
                    self.rbt.update_pointer(self.heap[idx]["ride"][0],idx)
                    idx = self.parent(idx)
                else:
                    break
        # if new trip duration is more than old trip duration but less than  2*old duration
        # first remove the ride from both minheap and rbt, then add the rides with new trip duration and increase ridecost by 10
        elif new_tripduration > old_tripduration and new_tripduration <= 2*old_tripduration:
            self.deleteride(existing_ride[0])
            self.insert((existing_ride[0],existing_ride[1]+10,new_tripduration))
        # if new trip is more than 2*oldtripduration, just delete the ride implying ride declined
        else:
            self.deleteride(existing_ride[0])
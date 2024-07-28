from filewriter import File
#red black tree implementation
class RBT:
    class Node: 
        #red black tree node stores ride information, node color-Red or Black
        # ridenumber is the key, left and right pointers, and pointer to location of the node in minheap
        def __init__(self,ridenumber,ridetriplet):
            self.ridetriplet = ridetriplet
            self.ridenumber = ridenumber
            self.left = None
            self.right = None
            self.color = 'R'
            self.pointer = None
    def __init__(self):
        self.root = None # we traverse tree through root node. It will be the first node of the tree
        self.output_file = File() # to write output to output_file.txt
        
    #performs left rotate 
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        y.color = x.color
        x.color = 'R'
        return y
    #performs right rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        y.color = x.color
        x.color = 'R'
        return y

    # flips colors of the node and its children so that parent and child nodes are not both stored as red nodes
    def flipcolors(self, node):
        node.color='R'
        node.left.color ='B'
        node.right.color ='B'
    
    #inserts node into red black tree(recursive)
    def insert_helper(self, node, ridenumber, ridetriplet):
        #searching external node in red black tree to place the ride
        if node == None:
            return self.Node(ridenumber,ridetriplet) # if external null node found, place the node there
        if ridenumber < node.ridenumber:
            node.left = self.insert_helper(node.left,ridenumber,ridetriplet)
        elif ridenumber > node.ridenumber:
            node.right = self.insert_helper(node.right,ridenumber,ridetriplet)
        else:
            exit() #if ride with same ride number found, it is a duplicate, so exit the program
        
        #red black tree insert cases
        if not self.check_red(node.left) and self.check_red(node.right):
            node = self.left_rotate(node)
        if self.check_red(node.left) and self.check_red(node.left.left):
            node = self.right_rotate(node)
        if self.check_red(node.left) and self.check_red(node.right):
            self.flipcolors(node)
        return node
    
    def insert(self, ridenumber,ridetriplet):
        self.root = self.insert_helper(self.root, ridenumber,ridetriplet) #getting root of tree formed after inserting ridetriplet
        self.root.color = 'B' #root of rbtree should always be black

    #function to update pointer in red black tree to the position(index) of the given ride in minheap
    def update_pointer(self,ridenumber,pointer_to_minheap):
        tmp = self.root
        while self.root != None:
            if ridenumber==self.root.ridenumber:
                self.root.pointer = pointer_to_minheap
                break
            elif ridenumber > self.root.ridenumber:
                self.root=self.root.right
            else:
                self.root = self.root.left
        self.root = tmp
    
    # find node with minimum ridenumber in the red black tree rooted at node passed to the function.
    # in a red black tree, smallest node is always the left most node
    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    #red black tree delete operation (recursive)
    def delete_node_helper(self, node, ridenumber):
        #search for ride(node) to delete
        if node == None:
            return None  # if node to delete is not present in the tree
        if ridenumber < node.ridenumber:
            node.left = self.delete_node_helper(node.left,ridenumber)
        elif ridenumber > node.ridenumber:
            node.right = self.delete_node_helper(node.right,ridenumber)
        else:
            if node.left == None:
                return node.right #if node to be deleted does not have a left child 
            elif node.right == None:
                return node.left # if node to be deleted does not have a right child
            else:
                #if the node to be deleted has both left and ride children
                #replace the node to be deleted with the smallest node in its right subtree
                replacement_node = self.minimum(node.right)
                node.ridenumber = replacement_node.ridenumber
                node.ridetriplet = replacement_node.ridetriplet
                node.pointer = replacement_node.pointer
                node.right = self.delete_node_helper(node.right,replacement_node.ridenumber)
        
        #red black tree delete cases handling
        if not self.check_red(node.left) and self.check_red(node.right):
            node = self.left_rotate(node)
        if self.check_red(node.left) and self.check_red(node.left.left):
            node = self.right_rotate(node)
        if self.check_red(node.left) and self.check_red(node.right):
            self.flipcolors(node)
        return node
    
    # check if node is red
    def check_red(self,x):
        if x is None:
            return False
        if x.color=='R':
            return True
        else:
            return False
    
    # get root of red black tree after deleting the given node from the red black tree
    def delete(self,ridenumber):
        self.root = self.delete_node_helper(self.root,ridenumber)
        
    # searches for a given node and returns the ride triplet and pointer to its index in minheap
    def find(self,ridenumber):
        ride = self.root
        while ride != None:
            if ridenumber == ride.ridenumber:
                return ride.ridetriplet,ride.pointer
            elif ridenumber > ride.ridenumber:
                ride = ride.right
            else:
                ride = ride.left
        return None,None #if node not found
    
    # update tripduration function. This function handles the case for rbt when new trip duratio is less than old trp duration
    # The other 2 cases are handled by the delete and insert functions based on the update conditions
    def updatetripduration(self,ridenumber,new_tripduration):
        tmp = self.root
        # search for node whose trip duration to update
        while self.root.ridenumber !=None:
            if ridenumber==self.root.ridenumber:
                new_node = (self.root.ridetriplet[0],self.root.ridetriplet[1],new_tripduration)
                self.root.ridetriplet = new_node # update trip duration of ride
                break
            elif ridenumber > self.root.ridenumber:
                self.root=self.root.right
            else:
                self.root = self.root.left
        self.root = tmp # get back to the root of the tree
        
    #recursive inorder traversal to get nodes within range [ridenumber1,ridenumber2]
    def get_inorder(self,node,res,ridenumber1,ridenumber2): 
        if node is not None:
            if ridenumber1 < node.ridenumber:
                self.get_inorder(node.left,res,ridenumber1,ridenumber2)
            if ridenumber1 <= node.ridenumber and ridenumber2>=node.ridenumber:
                res.append(node)
            if ridenumber2 > node.ridenumber:
                self.get_inorder(node.right,res,ridenumber1,ridenumber2)
    
    # gets all rides present within a given range [ridenumber1,ridenumber2] 
    def getrides(self,ridenumber1,ridenumber2):
        res=[]
        self.get_inorder(self.root,res,ridenumber1,ridenumber2) # do inorder traversal because we want rides to be printed in ascending order 
        return res
        
        
    # handles printing all rides within a given range
    def printrides(self,ridenumber1,ridenumber2):
        allrides = ""
        rides = self.getrides(ridenumber1,ridenumber2)
        if len(rides)==0: #if no rides within given range
            data = ["(0,0,0)"]
            self.output_file.filewrite(data)
            print("(0,0,0)")
            return
        for ride in rides:
            allrides=allrides+"("+str(ride.ridetriplet[0])+","+str(ride.ridetriplet[1])+","+str(ride.ridetriplet[2])+"),"  
        data = [allrides[:-1]]
        self.output_file.filewrite(data)       #output all rides within given range 
        print(allrides[:-1])
        
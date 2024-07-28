#Output File Handler
class File:
    def __init__(self):
        self.outfilename = "output_file.txt"    
        file1 = open(self.outfilename,"w")  #deleting any old content in output_file.txt
        file1.close()
    
    def filewrite(self,data):
        with open(self.outfilename,"a") as outfile:
            outfile.writelines(data)                # appending output lines to output_file.txt
            outfile.writelines('\n')
        

        
        
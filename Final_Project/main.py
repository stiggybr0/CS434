import sys
import csv

'''
Created on Oct 30, 2012

@author: James Cunningham & Andy Miller
'''


'''
Function: main
Purpose: Check usage and execute menu()
Input: N/A
Output: N/A
'''
def main():
    if(len(sys.argv) != 2):
        print "Incorrect number of arguments."
        print "Usage: python main.py 434FP.csv" 
        sys.exit()
        
    menu()
    
'''
Function:init_vectors
Purpose: adds raw input into list to build vectors.
Input: raw sys.arg
Output: Array of points
'''
def init_vectors(csv_data):
    vector_list=[]
    cluster_file = csv.reader(open(csv_data, "rt"))
    for line in cluster_file:
        vector_list.append(line)
        print line
        
    #print vector_list  
    return vector_list  
    
'''
Function: menu
Purpose: handle user input, output to text files, calculate accuracies
Input: N/A
Output: write to files.
'''
def menu():
    csv_data = sys.argv[1]
    count = 0
    while count == 0:
        print """
What would you like to do?
0) Exit
1) See work so far"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            print "Initializing vectors."
            vector_list = init_vectors(csv_data)                              
            print "-------------------------------------------------"
              
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()
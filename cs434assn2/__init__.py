import sys
import random

'''
Created on Oct 15, 2012

@author: James Cunningham & Andy Miller
'''


'''
Function: main
Purpose: Check usage and execute menu()
Input: N/A
Output: N/A
'''

def main():
    if(len(sys.argv) != 3):
        print "Incorrect number of arguments."
        print "Usage: python main.py tn-train.txt tn-test.txt" 
        sys.exit()
    














'''
Function: menu
Purpose: handle user input, output to text files, calculate accuracies
Input: N/A
Output: write to files.
'''

def menu():
    training_data = sys.argv[1]
    testing_data = sys.argv[2]
    count = 0
    while count == 0:
        print """
What would you like to do?
0) Exit
1) 
2) """
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            
        elif action == str(2):
            print "-------------------------------------------------"
            
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."


'''
Execute Main
'''

if __name__ == '__main__':
    main()
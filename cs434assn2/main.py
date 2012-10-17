import sys
import csv
import math

'''
Created on Oct 16, 2012

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
        print "Usage: python main.py monks-1-test.csv monks-1-train.csv" 
        sys.exit()
    menu()
    
    
'''
Function: value_init
Purpose: static training algorithm
Input: CSV of monk data.
Output: 2d array with values and probabilities.
'''
    
def value_init(csvname):
    datamap = []
    classline = []
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    line6 = []
    
    csvmap = csv.reader(open(csvname))
    
    for row in csvmap:
        classify, x1, x2, x3, x4, x5, x6 = [int(x) for x in row] 
        classline.append(classify)
        line1.append(x1)
        line2.append(x2)
        line3.append(x3)
        line4.append(x4)
        line5.append(x5)
        line6.append(x6)

    datamap.append(classline)
    datamap.append(line1)
    datamap.append(line2)
    datamap.append(line3)
    datamap.append(line4)
    datamap.append(line5)
    datamap.append(line6)

    return datamap

'''
Function: entropy_calc
Purpose: Calculate entropies of each data set
Input: datamap of initialized CSVs
Output: appended entropies
'''

def entropy_calc(datamap):
    counter = 0
    entropylist = []
    entropyval = 0.0
    prob = []
    for  list in datamap:
        if (counter != 0):
            # Initialize Probability Variables
            if(counter == 1 or counter == 2 or counter == 4):
                prob = [0] * 3
            elif(counter == 3 or counter == 6):
                prob = [0] * 2
            elif(counter == 5):
                prob = [0] * 4
            else:
                print "Sanity Check: Failed!"
            for item in list:
                prob[item-1] = prob[item-1] + 1
            prob[:] = [float(x)/float(len(list)) for x in prob] 
        
            for item in prob:
                entropyval = entropyval - item*(math.log(item)/math.log(float(len(prob))))
            print entropyval
        
        counter = counter + 1
    
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
1) See work so far"""
        action = raw_input("> ")
        if action == str(1):
            print "-------------------------------------------------"
            dmap = value_init(training_data) 
            entropy_calc(dmap)                                                                     
            print "-------------------------------------------------"
              
        elif action == str(0):
            sys.exit()
        else:
            print "Invalid input. Try again ....."
            
            
if __name__ == '__main__':
    main()